from Workflows.testfullnodesanddatasource.testfullnodesanddatasource import function_1, function_2, function_3, function_4, function_5, function_6import pytest
from unittest.mock import MagicMock

def test_testfullnodesanddatasource_intent_positive():
    # Arrange
    payload = {
        'chatConversation': [
            {
                'data': {'content': '', 'contentType': 'txt'},
                'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1},
                'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'},
                'order': 1,
                'role': 'user'
            }
        ],
        'metaData': {
            'conversationID': 'test-conv-id',
            'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''},
            'intent': 'Passwordresetautomation',
            'userData': {
                'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7',
                'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f',
                'phoneNo': '+91-877-817-8737',
                'userEmail': 'emilywilson@avatest.in',
                'user_name': 'emily'
            }
        }
    }

    # Mock required functions
    with monkeypatch.context() as m:
        m.setattr('testfullnodesanddatasource_intent.getLanguage', lambda x: 'Language response')
        m.setattr('testfullnodesanddatasource_intent.process_functions', lambda *args: 'Success')

        # Act
        result = testfullnodesanddatasource_intent(payload)

        # Assert
        assert result == 'Success'
        assert payload['chatConversation'][-1]['data']['content'] == 'Language response'

def test_testfullnodesanddatasource_intent_negative():
    # Arrange
    payload = {
        'chatConversation': [
            {
                'data': {'content': '', 'contentType': 'txt'},
                'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1},
                'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'},
                'order': 1,
                'role': 'user'
            }
        ],
        'metaData': {
            'conversationID': 'test-conv-id',
            'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''},
            'intent': 'Passwordresetautomation',
            'userData': {
                'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7',
                'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f',
                'phoneNo': '+91-877-817-8737',
                'userEmail': 'emilywilson@avatest.in',
                'user_name': 'emily'
            }
        }
    }

    # Mock required functions
    with monkeypatch.context() as m:
        m.setattr('testfullnodesanddatasource_intent.getLanguage', lambda x: 'Language response')
        m.setattr('testfullnodesanddatasource_intent.process_functions', lambda *args: Exception('Error occurred'))

        # Act
        result = testfullnodesanddatasource_intent(payload)

        # Assert
        assert result == 'An Unexpected error occurred. Please try again later.'
        assert payload['chatConversation'][-1]['data']['content'] == 'Language response'

@pytest.mark.parametrize('payload', [
    {
        'chatConversation': [],
        'metaData': {
            'conversationID': 'test-conv-id',
            'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''},
            'intent': 'Passwordresetautomation',
            'userData': {
                'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7',
                'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f',
                'phoneNo': '+91-877-817-8737',
                'userEmail': 'emilywilson@avatest.in',
                'user_name': 'emily'
            }
        }
    },
    {
        'chatConversation': [
            {
                'data': {'content': '', 'contentType': 'txt'},
                'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1},
                'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'},
                'order': 1,
                'role': 'user'
            }
        ],
        'metaData': {}
    }
])
def test_testfullnodesanddatasource_intent_invalid_payload(payload):
    # Mock required functions
    with monkeypatch.context() as m:
        m.setattr('testfullnodesanddatasource_intent.getLanguage', lambda x: 'Language response')
        m.setattr('testfullnodesanddatasource_intent.process_functions', lambda *args: 'Success')

        # Act
        result = testfullnodesanddatasource_intent(payload)

        # Assert
        assert result == 'An Unexpected error occurred. Please try again later.'
import pytest
from unittest.mock import patch

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_func(message, payload, order):
        payload['chatConversation'].append({'data': {'content': message}, 'order': order, 'role': 'assistant'})
        return payload
    monkeypatch.setattr("__main__.handle_success_response_text", mock_func)

def test_function_0_positive(payload_sample, mock_handle_success_response_text):
    payload = payload_sample
    result = function_0(payload)
    assert result['chatConversation'][-1]['data']['content'] == 'Welcome to the superdesk!'
    assert len(result['chatConversation']) == 2

def test_function_0_negative(payload_sample, mock_handle_success_response_text):
    payload = payload_sample
    payload['chatConversation'][-1]['data']['content'] = 'Invalid input'
    result = function_0(payload)
    assert result['chatConversation'][-1]['data']['content'] == 'Welcome to the superdesk!'
    assert len(result['chatConversation']) == 2

def test_function_0_empty_input(payload_sample, mock_handle_success_response_text):
    payload = payload_sample
    payload['chatConversation'][-1]['data']['content'] = ''
    result = function_0(payload)
    assert result['chatConversation'][-1]['data']['content'] == 'Welcome to the superdesk!'
    assert len(result['chatConversation']) == 2

def test_function_0_no_conversation(monkeypatch, mock_handle_success_response_text):
    payload = {}
    with pytest.raises(KeyError):
        function_0(payload)
import pytest
from unittest.mock import patch

@pytest.fixture
def payload_data():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('function_2.handle_success_response_options')
@patch('function_2.DB_access')
@patch('function_2.getRequest')
@patch('function_2.handle_success_response_dropdown')
@patch('function_2.handle_success_response_date')
@patch('function_2.handle_success_response_text')
@patch('function_2.LLM_call')
@patch('function_2.vector_db')
def test_function_2_positive(mock_vector_db, mock_LLM_call, mock_handle_success_response_text, mock_handle_success_response_date, mock_handle_success_response_dropdown, mock_getRequest, mock_DB_access, mock_handle_success_response_options, payload_data):
    mock_handle_success_response_options.return_value = payload_data
    mock_DB_access.return_value = {'user_details': 'test_details'}
    mock_getRequest.return_value = {'value': 'test_fetch'}
    mock_handle_success_response_dropdown.return_value = payload_data
    mock_handle_success_response_date.return_value = payload_data
    mock_handle_success_response_text.return_value = payload_data
    mock_LLM_call.return_value = {'choice': 'test_response'}
    mock_vector_db.return_value = {'response': 'test_request'}

    result = function_2(payload_data)

    assert result == payload_data

@patch('function_2.handle_success_response_options')
def test_function_2_negative_no_response(mock_handle_success_response_options, payload_data):
    mock_handle_success_response_options.return_value = {'user_choice': 'no'}

    result = function_2(payload_data)

    assert result == payload_data

@patch('function_2.DB_access')
def test_function_2_negative_db_error(mock_DB_access, payload_data):
    mock_DB_access.side_effect = Exception('Database Error')

    with pytest.raises(Exception, match='Database Error'):
        function_2(payload_data)

@patch('function_2.getRequest')
def test_function_2_negative_api_error(mock_getRequest, payload_data):
    mock_getRequest.side_effect = Exception('API Error')

    with pytest.raises(Exception, match='API Error'):
        function_2(payload_data)
import pytest
from unittest.mock import patch

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    def mock_func(response_text, payload, End):
        return payload
    monkeypatch.setattr('function_3.handle_success_response_text', mock_func)

def test_function_3_positive(payload_fixture, mock_handle_success_response_text):
    payload = payload_fixture
    result = function_3(payload)
    assert result == payload

def test_function_3_negative_empty_payload(mock_handle_success_response_text):
    payload = {}
    with pytest.raises(KeyError):
        function_3(payload)

def test_function_3_negative_missing_chatconversation(mock_handle_success_response_text):
    payload = {'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}
    with pytest.raises(KeyError):
        function_3(payload)

def test_function_3_negative_empty_chatconversation(mock_handle_success_response_text):
    payload = {'chatConversation': []}
    with pytest.raises(IndexError):
        function_3(payload)

def test_function_3_negative_missing_data(mock_handle_success_response_text):
    payload = {'chatConversation': [{'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}]}
    with pytest.raises(KeyError):
        function_3(payload)import pytest
from unittest.mock import patch

@pytest.fixture
def sample_payload():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('function_1.handle_success_response_text')
@patch('function_1.handle_success_response_multichoice')
@patch('function_1.postRequest')
@patch('function_1.DB')
def test_function_1_positive(mock_db, mock_post_request, mock_multichoice, mock_text, sample_payload):
    mock_text.side_effect = [sample_payload, sample_payload]
    mock_multichoice.return_value = sample_payload
    mock_post_request.return_value = {'action': 'user_created'}
    mock_db.return_value = True

    result = function_1(sample_payload)

    assert result['chatConversation'][-1]['data']['content'] == 'Thank you for using Superdesk!'

def test_function_1_negative_invalid_payload(sample_payload):
    invalid_payload = {'invalid': 'payload'}

    with pytest.raises(KeyError):
        function_1(invalid_payload)

@patch('function_1.postRequest')
def test_function_1_negative_api_failure(mock_post_request, sample_payload):
    mock_post_request.return_value = {'error': 'API failure'}

    with pytest.raises(Exception):
        function_1(sample_payload)

@patch('function_1.DB')
def test_function_1_negative_db_failure(mock_db, sample_payload):
    mock_db.return_value = False

    with pytest.raises(Exception):
        function_1(sample_payload)
import pytest
from unittest.mock import patch

@pytest.fixture
def sample_payload():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_button(monkeypatch):
    def mock_func(*args):
        return args[3]
    monkeypatch.setattr('function_End.handle_success_response_button', mock_func)

@pytest.fixture
def mock_handle_success_response_multichoice(monkeypatch):
    def mock_func(*args):
        return args[3]
    monkeypatch.setattr('function_End.handle_success_response_multichoice', mock_func)

def test_function_End_positive(sample_payload, mock_handle_success_response_button, mock_handle_success_response_multichoice):
    payload = sample_payload
    result = function_End(payload)
    assert result == payload

def test_function_End_negative_empty_chatconversation(sample_payload, mock_handle_success_response_button, mock_handle_success_response_multichoice):
    payload = sample_payload
    payload['chatConversation'] = []
    with pytest.raises(IndexError):
        function_End(payload)

def test_function_End_negative_missing_data(sample_payload, mock_handle_success_response_button, mock_handle_success_response_multichoice):
    payload = sample_payload
    del payload['chatConversation'][0]['data']
    with pytest.raises(KeyError):
        function_End(payload)

def test_function_End_negative_missing_content(sample_payload, mock_handle_success_response_button, mock_handle_success_response_multichoice):
    payload = sample_payload
    del payload['chatConversation'][0]['data']['content']
    with pytest.raises(KeyError):
        function_End(payload)