from datetime import datetime

txt_response = {"contentType": "txt", "content": ""}

chat_conversation_response = {
    "order": 1,
    "role": "bot",
    "meta": {
        "name": "Service Help Desk AI BOT",
        "timeStamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
    },
    "data": {},

}





# link=
button_obj={
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "text"
            }
        },
        {
            "type": "actions",
            "elements": [
                
             ]
         }
     ]
 }
 
dropdown={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Pick an item from the dropdown list"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": False
				},
				"options": [
					
				],
				"action_id": "static_select-action"
			}
		}
	]
}


date_picker={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ""
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": False
				},
				"action_id": "datepicker-action"
			}
		}
	]
}


card={
	"blocks": [
		{
			"type": "section",
			"fields": [
				{
					"type": "plain_text",
					"text": "*this is plain_text text*",
					"emoji": True
				},
				{
					"type": "plain_text",
					"text": "*this is plain_text text*",
					"emoji": True
				},
				{
					"type": "plain_text",
					"text": "*this is plain_text text*",
					"emoji": True
				},
				{
					"type": "plain_text",
					"text": "*this is plain_text text*",
					"emoji": True
				},
				{
					"type": "plain_text",
					"text": "*this is plain_text text*",
					"emoji": True
				}
			]
		}
	]
}


radio={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select any of the options"
			},
			"accessory": {
				"type": "radio_buttons",
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "yes",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No",
							"emoji": True
						},
						"value": "value-1"
					}
				],
				"action_id": "radio_buttons-action"
			}
		}
	]
}                                                                                                                                                                                             or proceeding with  buttons json


multichoice={
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "This is a section block with checkboxes."
			},
			"accessory": {
				"type": "checkboxes",
				"options": [
					{
						"text": {
							"type": "mrkdwn",
							"text": "AI"
						},
						"description": {
							"type": "mrkdwn",
							"text": "python, react"
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"description": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"description": {
							"type": "mrkdwn",
							"text": "*this is mrkdwn text*"
						},
						"value": "value-2"
					}
				],
				"action_id": "checkboxes-action"
			}
		}
	]
}


# choice_options: {"options": "", "selected": False}
