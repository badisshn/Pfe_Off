from odoo16.odoo16.odoo import models, fields
import requests


# Inherit livechat.channel model
class LivechatChannelInherit(models.Model):
    _inherit = 'im_livechat'


chat_integration_key = fields.Char(string='Chat Integration Key')


@api.model
def get_chat_response(self, message):
    # Call ChatGPT API to get response
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": message,
        "max_tokens": 150
    }
    response = requests.post(url, headers=headers, json=payload)
    response_data = response.json()
    chat_response = response_data['choices'][0]['text'].strip()

    return chat_response
