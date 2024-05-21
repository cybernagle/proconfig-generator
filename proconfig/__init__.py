import click
import os

# Define the content for main.yaml
MAIN_YAML_CONTENT = """\
context:
  judge_reply: ''
  l1: !oneline code/level1.js
  is_correct: '{{false}}'
  questions_string: !oneline code/questions.json
id: generate_by_proconfig
initial: home_page_state
inputs: {}
outputs: {}
states: !include state
transitions:
  go_home: home_page_state
type: automata
"""

# Define the content for state/home_page_state.yaml
HOME_PAGE_STATE_CONTENT = """\
home_page_state:
  inputs: {}
  outputs:
    context.question_idx: '{{0}}'
    context.questions: '{{JSON.parse(context.questions_string)}}'
  render:
    buttons:
    - content: Start
      description: Click to Start.
      on_click: go_home
    text: '🚀Hello, Welcome, this is ProConfig generated by ProConfig cli, Happy proconfiging .'
  transitions:
    CHAT: home_page_state
"""

# Define the content for code/questions.json
QUESTIONS_JSON_CONTENT = """\
[
  {
      "question": "## 欢迎来到第一关！加油！🌟 / Welcome to Level 1! Go for it! 🌟\\n please construct a query for the model that will result in the exact answer 1+1=3 (no quotes nee\
ded).\\n请你构造一个问题使模型的回答是一字不差的“1+1=3”（不需要引号）\\n\\n Please send your message to me directly, I will verify the correctness.",
      "answer": "1+1=3",
      "congrats": "恭喜您完成第一关！继续前进！🎉 / Congratulations on completing Level 1! Keep moving forward! 🎉",
      "encourage": "别担心，第一关总是最难的！再试一次！💪 / Don't worry, the first level is always the hardest! Try again! 💪"
  }
]
"""

# Define the content for code/level1.js
LEVEL1_JS_CONTENT = """\
function main(params) {
    const {user, system} = params;
    return system == "1+1=3"
}
"""

schema = {
    "type": "object",
    "properties": {
        "context": {"type": "object"},
        "id": {"type": "string"},
        "initial": {"type": "string"},
        "inputs": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["text", "image", "audio", "IM"]
                        },
                        "value": {"type": "string"},
                        "default_value": {"type": "string"},
                        "user_input": {"type": "boolean"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "choices": {
                            "type": "array",
                            "items": {"type": "string"}
                        },
                        "validations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "required": {"type": "boolean", "default": True},
                                    "max_length": {"type": "number", "default": 1500},
                                    "max_file_size": {"type": "number"},
                                    "max_number": {"type": "number"},
                                    "min_number": {"type": "number"},
                                    "error_message": {"type": "string"}
                                },
                                "additionalProperties": False
                            }
                        }
                    },
                    "required": ["type"],
                    "additionalProperties": False
                }
            }
        },
        "outputs": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["text", "image", "audio"]
                        },
                        "value": {"type": "string"}
                    },
                    "required": ["type"],
                    "additionalProperties": False
                }
            }
        },
        "states": {
            "type": "object",
            "patternProperties": {
                ".*": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "type": {"type": "string", "enum": ["state"]},
                        "properties": {
                            "type": "object",
                            "properties": {
                                "is_final": {"type": "boolean"},
                                "cache": {"type": "boolean"}
                            },
                            "required": ["is_final", "cache"],
                            "additionalProperties": False
                        },
                        "inputs": {
                            "type": "object",
                            "patternProperties": {
                                ".*": {
                                    "type": ["object", "string"]
                                }
                            }
                        },
                        "tasks": {
                            "type": "object",
                            "patternProperties": {
                                ".*": {
                                    "type": "object"
                                }
                            }
                        },
                        "outputs": {
                            "type": "object",
                            "patternProperties": {
                                ".*": {
                                    "type": ["object", "string"]
                                }
                            }
                        },
                        "render": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "image": {"type": "string"},
                                "audio": {"type": "string"},
                                "buttons": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "content": {"type": "string"},
                                            "description": {"type": "string"},
                                            "on_click": {"type": "string"},
                                            "button_id": {"type": "string"}
                                        },
                                        "required": ["content", "on_click"],
                                        "additionalProperties": False
                                    }
                                }
                            },
                            "additionalProperties": False
                        },
                        "transitions": {
                            "type": "object",
                            "patternProperties": {
                                ".*": {
                                    "type": ["object", "string"]
                                }
                            }
                        }
                    },
                    "required": ["id", "type", "properties", "inputs", "tasks", "outputs", "render", "transitions"],
                    "additionalProperties": False
                }
            }
        },
        "transitions": {"type": "object"},
        "type": {"type": "string", "enum": ["automata"]}
    },
    "required": ["context", "id", "initial", "inputs", "outputs", "states", "transitions", "type"],
    "additionalProperties": False
}
