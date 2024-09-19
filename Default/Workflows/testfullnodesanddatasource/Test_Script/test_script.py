from Workflows.testfullnodesanddatasource.testfullnodesanddatasource import function_1, function_2, function_3, function_4, function_5, function_6import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def payload_data():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('testfullnodesanddatasource_intent.getLanguage', return_value='mock_language_response')
@patch('testfullnodesanddatasource_intent.process_functions', return_value='mock_process_result')
def test_testfullnodesanddatasource_intent_positive(payload_data, monkeypatch):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    result = testfullnodesanddatasource_intent(payload_data)
    assert result == 'mock_process_result'

def test_testfullnodesanddatasource_intent_negative_invalid_payload(payload_data, monkeypatch):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    payload_data.pop('metaData')
    result = testfullnodesanddatasource_intent(payload_data)
    assert result == 'An Unexpected error occurred. Please try again later.'

def test_testfullnodesanddatasource_intent_negative_invalid_conversationid(payload_data, monkeypatch):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    payload_data['metaData']['conversationID'] = None
    result = testfullnodesanddatasource_intent(payload_data)
    assert result == 'An Unexpected error occurred. Please try again later.'

def test_testfullnodesanddatasource_intent_negative_exception(payload_data, monkeypatch):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    monkeypatch.setattr('testfullnodesanddatasource_intent.process_functions', lambda *args, **kwargs: 1/0)
    result = testfullnodesanddatasource_intent(payload_data)
    assert result == 'An Unexpected error occurred. Please try again later.'import pytest
from unittest.mock import patch

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

def function_0(payload):
    userPrompt=payload["Chatconversation"][-1]["data"]["content"]
    payload=handle_success_response_text("Welcome to the superdesk!", payload, 1)
    return payload

@patch('__main__.handle_success_response_text')
def test_function_0_positive(mock_handle_success_response_text, payload_sample):
    mock_handle_success_response_text.return_value = payload_sample
    payload = function_0(payload_sample)
    assert payload == payload_sample

def test_function_0_negative(payload_sample):
    payload_sample['chatConversation'][0]['data']['content'] = 'Invalid prompt'
    with pytest.raises(KeyError):
        function_0(payload_sample)

def test_function_0_empty_payload():
    empty_payload = {}
    with pytest.raises(KeyError):
        function_0(empty_payload)import pytest
from unittest.mock import patch

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.mark.parametrize("user_choice, expected_result", [('yes', True), ('no', False)])
def test_handle_success_response_options(monkeypatch, payload_fixture, user_choice, expected_result):
    monkeypatch.setattr('function_2.handle_success_response_options', lambda *args: user_choice)
    payload = payload_fixture
    payload = function_2(payload)
    assert ('user choice' in payload['chatConversation'][-1]['data']['content']) == expected_result

@pytest.mark.parametrize("db_response, get_api_response, llm_response, vb_response", [({'user_details': 'test_data'}, {'value': 'test_value'}, {'choice': 'test_choice'}, {'response': 'test_response'})])
def test_function_2_positive(monkeypatch, payload_fixture, db_response, get_api_response, llm_response, vb_response):
    monkeypatch.setattr('function_2.DB_access', lambda *args: db_response)
    monkeypatch.setattr('function_2.getRequest', lambda *args: get_api_response)
    monkeypatch.setattr('function_2.LLM_call', lambda *args: llm_response)
    monkeypatch.setattr('function_2.vector_db', lambda *args: vb_response)
    monkeypatch.setattr('function_2.handle_success_response_options', lambda *args: 'yes')
    payload = payload_fixture
    result = function_2(payload)
    assert result['chatConversation'][-1]['data']['content'] == 'test_response'

def test_function_2_negative(monkeypatch, payload_fixture):
    monkeypatch.setattr('function_2.handle_success_response_options', lambda *args: 'no')
    payload = payload_fixture
    result = function_2(payload)
    assert 'user choice' not in result['chatConversation'][-1]['data']['content']import pytest
from unittest.mock import patch

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_function(text, payload, End):
        return payload
    monkeypatch.setattr('function_3.handle_success_response_text', mock_function)

def test_function_3_positive(payload_fixture, mock_handle_success_response_text):
    payload = payload_fixture
    expected_output = payload
    result = function_3(payload)
    assert result == expected_output

def test_function_3_negative_empty_chatConversation(mock_handle_success_response_text):
    payload = {'chatConversation': [], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}
    with pytest.raises(IndexError):
        function_3(payload)

def test_function_3_negative_missing_content(payload_fixture, mock_handle_success_response_text):
    payload = payload_fixture
    payload['chatConversation'][0]['data'].pop('content')
    with pytest.raises(KeyError):
        function_3(payload)import pytest
from unittest.mock import patch

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_response(text, payload, index):
        payload['chatConversation'].append({'data': {'content': text}, 'order': index})
        return payload
    monkeypatch.setattr('function_1.handle_success_response_text', mock_response)

@pytest.fixture
def mock_handle_success_response_multichoice(monkeypatch):
    def mock_response(text, choices, payload, index):
        payload['chatConversation'].append({'data': {'content': text, 'choices': choices}, 'order': index})
        return payload
    monkeypatch.setattr('function_1.handle_success_response_multichoice', mock_response)

@pytest.fixture
def mock_post_request(monkeypatch):
    def mock_response(url, body, headers):
        return {'action': 'success'}
    monkeypatch.setattr('function_1.postRequest', mock_response)

@pytest.fixture
def mock_db(monkeypatch):
    def mock_response(query, variables):
        return 'success'
    monkeypatch.setattr('function_1.DB', mock_response)

def test_function_1_positive(payload_fixture, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_post_request, mock_db):
    payload = payload_fixture
    result = function_1(payload)
    assert len(result['chatConversation']) == 4
    assert result['chatConversation'][1]['data']['content'] == 'Enter your username'
    assert result['chatConversation'][2]['data']['content'] == 'select any of the choice'
    assert result['chatConversation'][2]['data']['choices'] == ['yes', 'no', 'default']
    assert result['chatConversation'][3]['data']['content'] == 'Thank you for using Superdesk!'

def test_function_1_negative_invalid_payload(payload_fixture, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_post_request, mock_db):
    payload = {}
    with pytest.raises(KeyError):
        function_1(payload)

def test_function_1_negative_empty_payload(payload_fixture, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_post_request, mock_db):
    payload = {'chatConversation': []}
    with pytest.raises(IndexError):
        function_1(payload)import pytest
from unittest.mock import patch

def handle_success_response_button(prompt, choices, payload, max_retries):
    return payload

def handle_success_response_multichoice(prompt, field, payload, max_retries):
    return payload

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('function_End.handle_success_response_button', side_effect=handle_success_response_button)
@patch('function_End.handle_success_response_multichoice', side_effect=handle_success_response_multichoice)
def test_function_End_positive(payload_fixture, monkeypatch):
    payload = payload_fixture
    payload['Chatconversation'][-1]['data']['content'] = 'test_content'
    result = function_End(payload)
    assert result == payload

def test_function_End_negative_empty_content(payload_fixture, monkeypatch):
    payload = payload_fixture
    result = function_End(payload)
    assert 'Chatconversation' in result
    assert len(result['Chatconversation'][-1]['data']['content']) == 0

def test_function_End_negative_no_chatconversation(payload_fixture, monkeypatch):
    payload = payload_fixture
    del payload['Chatconversation']
    with pytest.raises(KeyError):
        function_End(payload)
