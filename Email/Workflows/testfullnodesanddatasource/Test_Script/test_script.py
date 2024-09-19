from Workflows.testfullnodesanddatasource.testfullnodesanddatasource import function_1, function_2, function_3, function_4, function_5, function_6import pytest
from unittest.mock import MagicMock

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_functions():
    with pytest.MonkeyPatch.context() as m:
        m.setattr('testfullnodesanddatasource_intent.function_0', MagicMock())
        m.setattr('testfullnodesanddatasource_intent.function_1', MagicMock())
        m.setattr('testfullnodesanddatasource_intent.function_3', MagicMock())
        m.setattr('testfullnodesanddatasource_intent.function_4', MagicMock())
        m.setattr('testfullnodesanddatasource_intent.function_5', MagicMock())
        yield

# Positive Test Case
def test_testfullnodesanddatasource_intent_positive(payload_sample, mock_functions):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    payload = payload_sample
    result = testfullnodesanddatasource_intent(payload)
    assert result is not None

# Negative Test Case
def test_testfullnodesanddatasource_intent_negative(payload_sample, mock_functions):
    from testfullnodesanddatasource_intent import testfullnodesanddatasource_intent
    payload = payload_sample
    payload['metaData']['conversationID'] = None
    result = testfullnodesanddatasource_intent(payload)
    assert result == "An Unexpected error occurred. Please try again later."
import pytest
from unittest.mock import patch

@pytest.fixture
def sample_payload():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@patch('handle_success_response_text')
def test_function_0_positive(mock_handle_success_response_text, sample_payload):
    mock_handle_success_response_text.return_value = sample_payload
    payload = sample_payload
    result = function_0(payload)
    assert result == sample_payload
    mock_handle_success_response_text.assert_called_once_with('Welcome to the superdesk!', sample_payload, 1)

def test_function_0_negative_empty_payload(sample_payload):
    payload = {}
    with pytest.raises(KeyError):
        function_0(payload)

def test_function_0_negative_missing_chatConversation(sample_payload):
    del sample_payload['chatConversation']
    with pytest.raises(KeyError):
        function_0(sample_payload)

def test_function_0_negative_empty_chatConversation(sample_payload):
    sample_payload['chatConversation'] = []
    with pytest.raises(IndexError):
        function_0(sample_payload)import pytest
from unittest.mock import patch

@pytest.fixture
def payload_fixture():
    return {
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

@patch('function_2.handle_success_response_options')
@patch('function_2.DB_access')
@patch('function_2.getRequest')
@patch('function_2.handle_success_response_dropdown')
@patch('function_2.handle_success_response_date')
@patch('function_2.handle_success_response_text')
@patch('function_2.LLM_call')
@patch('function_2.vector_db')
def test_function_2_positive(mock_vector_db, mock_LLM_call, mock_handle_success_response_text, mock_handle_success_response_date, mock_handle_success_response_dropdown, mock_getRequest, mock_DB_access, mock_handle_success_response_options, payload_fixture):
    mock_handle_success_response_options.return_value = payload_fixture
    mock_DB_access.return_value = {'user_details': 'test_user_details'}
    mock_getRequest.return_value = {'value': 'test_fetch_value'}
    mock_handle_success_response_dropdown.return_value = payload_fixture
    mock_handle_success_response_date.return_value = payload_fixture
    mock_handle_success_response_text.return_value = payload_fixture
    mock_LLM_call.return_value = {'choice': 'test_llm_response'}
    mock_vector_db.return_value = {'response': 'test_vector_db_response'}

    result = function_2(payload_fixture)

    assert result == payload_fixture

@patch('function_2.handle_success_response_options')
def test_function_2_negative_handle_success_response_options(mock_handle_success_response_options, payload_fixture):
    mock_handle_success_response_options.return_value = None

    with pytest.raises(AttributeError):
        function_2(payload_fixture)

@patch('function_2.DB_access')
def test_function_2_negative_DB_access(mock_DB_access, payload_fixture):
    mock_DB_access.return_value = None

    with pytest.raises(TypeError):
        function_2(payload_fixture)

@patch('function_2.getRequest')
def test_function_2_negative_getRequest(mock_getRequest, payload_fixture):
    mock_getRequest.return_value = None

    with pytest.raises(TypeError):
        function_2(payload_fixture)

@patch('function_2.handle_success_response_dropdown')
def test_function_2_negative_handle_success_response_dropdown(mock_handle_success_response_dropdown, payload_fixture):
    mock_handle_success_response_dropdown.return_value = None

    with pytest.raises(AttributeError):
        function_2(payload_fixture)

@patch('function_2.handle_success_response_date')
def test_function_2_negative_handle_success_response_date(mock_handle_success_response_date, payload_fixture):
    mock_handle_success_response_date.return_value = None

    with pytest.raises(AttributeError):
        function_2(payload_fixture)

@patch('function_2.handle_success_response_text')
def test_function_2_negative_handle_success_response_text(mock_handle_success_response_text, payload_fixture):
    mock_handle_success_response_text.return_value = None

    with pytest.raises(AttributeError):
        function_2(payload_fixture)

@patch('function_2.LLM_call')
def test_function_2_negative_LLM_call(mock_LLM_call, payload_fixture):
    mock_LLM_call.return_value = None

    with pytest.raises(TypeError):
        function_2(payload_fixture)

@patch('function_2.vector_db')
def test_function_2_negative_vector_db(mock_vector_db, payload_fixture):
    mock_vector_db.return_value = None

    with pytest.raises(TypeError):
        function_2(payload_fixture)
import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def payload_fixture():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    mock_func = Mock(return_value={'status': 'success', 'payload': {'chatConversation': [{'data': {'content': 'thank you for using superdesk', 'contentType': 'txt'}}]}})
    monkeypatch.setattr('function_3.handle_success_response_text', mock_func)
    return mock_func

def test_function_3_positive(payload_fixture, mock_handle_success_response_text):
    result = function_3(payload_fixture)
    assert result == mock_handle_success_response_text.return_value['payload']

def test_function_3_negative_empty_payload(mock_handle_success_response_text):
    with pytest.raises(KeyError):
        function_3({})

def test_function_3_negative_missing_key(payload_fixture, mock_handle_success_response_text):
    del payload_fixture['chatConversation']
    with pytest.raises(KeyError):
        function_3(payload_fixture)

def test_function_3_negative_empty_chatConversation(payload_fixture, mock_handle_success_response_text):
    payload_fixture['chatConversation'] = []
    with pytest.raises(IndexError):
        function_3(payload_fixture)
import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def sample_payload():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.fixture
def mock_handle_success_response_text(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('function_1.handle_success_response_text', mock)
    return mock

@pytest.fixture
def mock_handle_success_response_multichoice(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('function_1.handle_success_response_multichoice', mock)
    return mock

@pytest.fixture
def mock_postRequest(monkeypatch):
    mock = MagicMock(return_value={'action': 'user_created'})
    monkeypatch.setattr('function_1.postRequest', mock)
    return mock

@pytest.fixture
def mock_DB(monkeypatch):
    mock = MagicMock(return_value={'status': 'success'})
    monkeypatch.setattr('function_1.DB', mock)
    return mock

def test_function_1_positive(sample_payload, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    result = function_1(sample_payload)
    assert mock_handle_success_response_text.call_count == 2
    assert mock_handle_success_response_multichoice.call_count == 1
    assert mock_postRequest.call_count == 1
    assert mock_DB.call_count == 1
    assert result['chatConversation'][-1]['data']['content'] == 'Thank you for using Superdesk!'

def test_function_1_negative_invalid_payload(mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    invalid_payload = {}
    with pytest.raises(KeyError):
        function_1(invalid_payload)

def test_function_1_negative_api_failure(sample_payload, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    mock_postRequest.return_value = {'error': 'API failure'}
    with pytest.raises(Exception):
        function_1(sample_payload)

def test_function_1_negative_db_failure(sample_payload, mock_handle_success_response_text, mock_handle_success_response_multichoice, mock_postRequest, mock_DB):
    mock_DB.return_value = {'status': 'failure'}
    with pytest.raises(Exception):
        function_1(sample_payload)import pytest
from unittest.mock import patch

def mock_handle_success_response_button(prompt, choices, payload, max_attempts):
    return payload

def mock_handle_success_response_multichoice(prompt, field, payload, max_attempts):
    return payload

@pytest.fixture
def payload_sample():
    return {'chatConversation': [{'data': {'content': '', 'contentType': 'txt'}, 'inputConfig': {'disableAttachment': 1, 'disableEmoji': 1, 'disableText': 0, 'disableVoice': 1, 'hiddenAttachment': 1, 'hiddenEmoji': 1, 'hiddenText': 0, 'hiddenVoice': 1}, 'meta': {'name': 'Superdesk', 'timeStamp': '2024-05-20T11:42:05.094Z'}, 'order': 1, 'role': 'user'}], 'metaData': {'conversationID': 'test-conv-id', 'entities': {'logged': {'count': '6', 'logged': 'logged_user', 'type': 'multiple'}, 'employeeIdValue': ''}, 'intent': 'Passwordresetautomation', 'userData': {'user_id': '36e42932-40f7-49b9-b9b6-edd8fa8daca7', 'organization_id': '577d3e38-3c68-4537-836f-0396b9991e3f', 'phoneNo': '+91-877-817-8737', 'userEmail': 'emilywilson@avatest.in', 'user_name': 'emily'}}}

@pytest.mark.parametrize('payload', [({'chatConversation': [{'data': {'content': 'Hello'}, 'meta': {'name': 'Superdesk'}}]}),
                                    ({'chatConversation': [{'data': {'content': ''}, 'meta': {'name': 'Superdesk'}}]}),
                                    ({'chatConversation': []})])
def test_function_End_positive(payload, monkeypatch):
    monkeypatch.setattr('function_End.handle_success_response_button', mock_handle_success_response_button)
    monkeypatch.setattr('function_End.handle_success_response_multichoice', mock_handle_success_response_multichoice)
    result = function_End(payload)
    assert result == payload

@pytest.mark.parametrize('payload', [({'chatConversation': []}),
                                    ({'chatConversation': [{'data': {}}]}),
                                    ({'chatConversation': [{'data': {'content': None}}]})])
def test_function_End_negative(payload, monkeypatch):
    monkeypatch.setattr('function_End.handle_success_response_button', mock_handle_success_response_button)
    monkeypatch.setattr('function_End.handle_success_response_multichoice', mock_handle_success_response_multichoice)
    with pytest.raises(Exception):
        function_End(payload)

def test_function_End_with_sample_payload(payload_sample, monkeypatch):
    monkeypatch.setattr('function_End.handle_success_response_button', mock_handle_success_response_button)
    monkeypatch.setattr('function_End.handle_success_response_multichoice', mock_handle_success_response_multichoice)
    result = function_End(payload_sample)
    assert result == payload_sample
