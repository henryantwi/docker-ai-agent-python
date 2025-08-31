from api.ai.llms import get_openai_llm

from api.ai.tools import send_me_email, get_unread_emails


EMAIL_TOOLS = {
    "send_me_email": send_me_email,
    "get_unread_emails": get_unread_emails,
}

def email_assistant(query: str):
    llm_base = get_openai_llm()
    
    # llm = llm_base.bind_tools([send_me_email, get_unread_emails]) # OR
    llm = llm_base.bind_tools(list(EMAIL_TOOLS.values()))

    messages = [
        (
            "system",
            "You are a helpful assistant for managing my email inbox.",
        ),
        ("human", f"{query}."),
    ]

    response = llm.invoke(messages)
    if hasattr(response, "tool_calls") and response.tool_calls:
        # Add the assistant's response with tool calls to the conversation
        messages.append(response)
        
        for tool_call in response.tool_calls:
            tool_name = tool_call.get("name")
            tool_func = EMAIL_TOOLS.get(tool_name)
            tool_args = tool_call.get("args")
            if not tool_func:
                continue
            tool_result = tool_func.invoke(tool_args)
            
            # Format tool result as a proper ToolMessage with required tool_call_id
            from langchain_core.messages import ToolMessage
            
            if isinstance(tool_result, dict):
                tool_content = f"Tool '{tool_name}' result: {tool_result}"
            else:
                tool_content = f"Tool '{tool_name}' result: {str(tool_result)}"
            
            tool_message = ToolMessage(
                content=tool_content,
                tool_call_id=tool_call.get("id", f"{tool_name}_call")
            )
            messages.append(tool_message)
        
        final_response = llm.invoke(messages)
        return final_response
    return response
