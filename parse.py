import json

def parse_agit_message(json_input: str, mention_type: str):
    data = json.loads(json_input, strict=False)
    msg = data.get("wall_message", {})
    user_info = msg.get("user", {})

    parsed_result = {
        "agit_id": user_info.get("agit_id", ""),
        "nickname": f"{user_info.get('nickname', '')}",
        "mension type": mention_type,
        "created_at": msg.get("created_at", ""),
        "message": msg.get('message', '')
    }

    return parsed_result

def to_markdown(parsed: dict) -> str:
    return f"""agit_id: {parsed["agit_id"]}
nickname:  {parsed["nickname"]}
mension type : {parsed["mension type"]}
created_at : {parsed["created_at"]}
message: 
```text
{parsed["message"]}
```
"""

if __name__ == '__main__':
    input_json = r'''
    {}
    '''

    mention_type = "personal"
    parsed = parse_agit_message(input_json, mention_type)
    print(to_markdown(parsed))