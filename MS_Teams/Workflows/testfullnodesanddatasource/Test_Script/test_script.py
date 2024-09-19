from Workflows.testfullnodesanddatasource.testfullnodesanddatasource import function_1, function_2, function_3, function_4, function_5, function_6import pytest
from unittest.mock import patch

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('testfullnodesanddatasource_intent.getLanguage')
@patch('testfullnodesanddatasource_intent.process_functions')
def test_positive_flow(mock_process_functions, mock_getLanguage, payload_sample):
    mock_getLanguage.return_value = 'language_response'
    mock_process_functions.return_value = 'success'
    payload = payload_sample
    result = testfullnodesanddatasource_intent(payload)
    assert result == 'success'

@patch('testfullnodesanddatasource_intent.getLanguage')
@patch('testfullnodesanddatasource_intent.process_functions')
def test_negative_flow_process_functions_error(mock_process_functions, mock_getLanguage, payload_sample):
    mock_getLanguage.return_value = 'language_response'
    mock_process_functions.side_effect = Exception('Error occurred')
    payload = payload_sample
    result = testfullnodesanddatasource_intent(payload)
    assert result == 'An Unexpected error occurred. Please try again later.'

def test_negative_flow_missing_metadata(payload_sample):
    payload = payload_sample
    del payload['metaData']
    with pytest.raises(KeyError):
        testfullnodesanddatasource_intent(payload)

def test_negative_flow_missing_conversation(payload_sample):
    payload = payload_sample
    del payload['chatConversation']
    with pytest.raises(IndexError):
        testfullnodesanddatasource_intent(payload)import pytest
from unittest.mock import patch

def handle_success_response_text(text, payload, order):
    payload['chatConversation'].append({
        'data': {'content': text, 'contentType': 'txt'},
        'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1},
        'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'},
        'order': order + 1,
        'role': 'assistant'
    })
    return payload

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.mark.parametrize('userPrompt, expected_response', [
    ('Hello', {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}, {'data': {'content': 'Welcome to the superdesk!', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 2, 'role': 'assistant'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}})],)
def test_function_0(payload_sample, userPrompt, expected_response, monkeypatch):
    monkeypatch.setattr('function_0.handle_success_response_text', handle_success_response_text)
    payload = payload_sample
    payload['chatConversation'][-1]['data']['content'] = userPrompt
    response = function_0(payload)
    assert response == expected_response

@pytest.mark.parametrize('userPrompt', ['', None])
def test_function_0_negative(payload_sample, userPrompt, monkeypatch):
    monkeypatch.setattr('function_0.handle_success_response_text', handle_success_response_text)
    payload = payload_sample
    payload['chatConversation'][-1]['data']['content'] = userPrompt
    with pytest.raises(KeyError):
        function_0(payload)import pytest
from unittest.mock import patch

@pytest.fixture
def sample_payload():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('function_2.handle_success_response_options', return_value={'Chatconversation': [{'data': {'content': 'yes'}}]})
@patch('function_2.DB_access', return_value={'user_details': 'test_user'})
@patch('function_2.getRequest', return_value={'value': 'test_value'})
@patch('function_2.handle_success_response_dropdown', return_value={'Chatconversation': [{'data': {'content': 'test_value'}}]})
@patch('function_2.handle_success_response_date', return_value={'Chatconversation': [{'data': {'content': '2023-05-20'}}]})
@patch('function_2.handle_success_response_text', return_value={'Chatconversation': [{'data': {'content': 'test_requirement'}}]})
@patch('function_2.LLM_call', return_value={'choice': 'test_llm_response'})
@patch('function_2.vector_db', return_value={'response': 'test_vb_response'})
def test_function_2_positive(mock_vector_db, mock_llm_call, mock_handle_text, mock_handle_date, mock_handle_dropdown, mock_get_request, mock_db_access, mock_handle_options, sample_payload):
    payload = function_2(sample_payload)
    assert payload['chatConversation'][-1]['data']['content'] == 'test_vb_response'

@patch('function_2.handle_success_response_options', return_value={'Chatconversation': [{'data': {'content': 'no'}}]})
def test_function_2_negative(mock_handle_options, sample_payload):
    payload = function_2(sample_payload)
    assert payload['chatConversation'][-1]['data']['content'] == ''

@patch('function_2.handle_success_response_options', return_value={'Chatconversation': [{'data': {'content': 'invalid'}}]})
def test_function_2_invalid_option(mock_handle_options, sample_payload):
    with pytest.raises(ValueError):
        function_2(sample_payload)
import pytest
from unittest.mock import patch

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_function(*args, **kwargs):
        return {'chatConversation': [{'data': {'content': 'thank you for using superdesk', 'contentType': 'txt'}}]}
    monkeypatch.setattr('function_3.handle_success_response_text', mock_function)

def test_function_3_positive(payload_sample, mock_handle_success_response_text):
    payload = payload_sample
    result = function_3(payload)
    assert result['chatConversation'][0]['data']['content'] == 'thank you for using superdesk'

def test_function_3_negative_empty_payload(mock_handle_success_response_text):
    payload = {}
    with pytest.raises(KeyError):
        function_3(payload)

def test_function_3_negative_no_chatconversation(mock_handle_success_response_text):
    payload = {'metaData': {'conversationID': 'test-conv-id'}}
    with pytest.raises(KeyError):
        function_3(payload)

def test_function_3_negative_empty_chatconversation(mock_handle_success_response_text):
    payload = {'chatConversation': []}
    with pytest.raises(IndexError):
        function_3(payload)import pytest
from unittest.mock import patch

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_response(*args, **kwargs):
        return kwargs['payload']
    monkeypatch.setattr('function_1.handle_success_response_text', mock_response)

@pytest.fixture
def mock_handle_success_response_multichoice(monkeypatch):
    def mock_response(*args, **kwargs):
        return kwargs['payload']
    monkeypatch.setattr('function_1.handle_success_response_multichoice', mock_response)

@pytest.fixture
def mock_postRequest(monkeypatch):
    def mock_response(*args, **kwargs):
        return {'action': 'success'}
    monkeypatch.setattr('function_1.postRequest', mock_response)

@pytest.fixture
def mock_DB(monkeypatch):
    def mock_response(*args, **kwargs):
        return 'success'
    monkeypatch.setattr('function_1.DB', mock_response)

def test_function_1_positive(payload_sample, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    result = function_1(payload_sample)
    assert result['chatConversation'][-1]['data']['content'] == 'Thank you for using Superdesk!'

def test_function_1_negative_invalid_payload(mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    invalid_payload = {}
    with pytest.raises(KeyError):
        function_1(invalid_payload)

def test_function_1_negative_invalid_response(payload_sample, mock_handle_success_response_text, mock_handle_success_response_multichoice, monkeypatch):
    def mock_invalid_postRequest(*args, **kwargs):
        return {}
    monkeypatch.setattr('function_1.postRequest', mock_invalid_postRequest)
    with pytest.raises(KeyError):
        function_1(payload_sample)

def test_function_1_negative_invalid_db_response(payload_sample, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, monkeypatch):
    def mock_invalid_DB(*args, **kwargs):
        raise Exception('Database Error')
    monkeypatch.setattr('function_1.DB', mock_invalid_DB)
    with pytest.raises(Exception):
        function_1(payload_sample)import pytest
from unittest.mock import patch

test_payload = {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

def handle_success_response_button(prompt, choices, payload, max_options):
    return payload

def handle_success_response_multichoice(prompt, field, payload, max_options):
    return payload

@pytest.fixture
def mock_handle_success_response_button(monkeypatch):
    monkeypatch.setattr('function_End.handle_success_response_button', handle_success_response_button)

@pytest.fixture
def mock_handle_success_response_multichoice(monkeypatch):
    monkeypatch.setattr('function_End.handle_success_response_multichoice', handle_success_response_multichoice)

@pytest.mark.parametrize('payload', [test_payload])
def test_function_End_positive(payload, mock_handle_success_response_button, mock_handle_success_response_multichoice):
    from function_End import function_End
    result = function_End(payload)
    assert isinstance(result, dict)
    assert 'chatConversation' in result
    assert 'metaData' in result

def test_function_End_negative_invalid_payload():
    from function_End import function_End
    invalid_payload = {}
    with pytest.raises(Exception):
        function_End(invalid_payload)

def test_function_End_negative_missing_key():
    from function_End import function_End
    invalid_payload = {'chatConversation': []}
    with pytest.raises(Exception):
        function_End(invalid_payload)