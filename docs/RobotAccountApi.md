# swagger_client.RobotAccountApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**projects_project_id_robots_get**](RobotAccountApi.md#projects_project_id_robots_get) | **GET** /projects/{project_id}/robots | Get all robot accounts of specified project
[**projects_project_id_robots_post**](RobotAccountApi.md#projects_project_id_robots_post) | **POST** /projects/{project_id}/robots | Create a robot account for project
[**projects_project_id_robots_robot_id_delete**](RobotAccountApi.md#projects_project_id_robots_robot_id_delete) | **DELETE** /projects/{project_id}/robots/{robot_id} | Delete the specified robot account
[**projects_project_id_robots_robot_id_get**](RobotAccountApi.md#projects_project_id_robots_robot_id_get) | **GET** /projects/{project_id}/robots/{robot_id} | Return the infor of the specified robot account.
[**projects_project_id_robots_robot_id_put**](RobotAccountApi.md#projects_project_id_robots_robot_id_put) | **PUT** /projects/{project_id}/robots/{robot_id} | Update status of robot account.


# **projects_project_id_robots_get**
> list[RobotAccount] projects_project_id_robots_get(project_id)

Get all robot accounts of specified project

Get all robot accounts of specified project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RobotAccountApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.

try:
    # Get all robot accounts of specified project
    api_response = api_instance.projects_project_id_robots_get(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotAccountApi->projects_project_id_robots_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 

### Return type

[**list[RobotAccount]**](RobotAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_post**
> projects_project_id_robots_post(project_id, robot)

Create a robot account for project

Create a robot account for project

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RobotAccountApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot = swagger_client.RobotAccountCreate() # RobotAccountCreate | Request body of creating a robot account.

try:
    # Create a robot account for project
    api_instance.projects_project_id_robots_post(project_id, robot)
except ApiException as e:
    print("Exception when calling RobotAccountApi->projects_project_id_robots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot** | [**RobotAccountCreate**](RobotAccountCreate.md)| Request body of creating a robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_delete**
> projects_project_id_robots_robot_id_delete(project_id, robot_id)

Delete the specified robot account

Delete the specified robot account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RobotAccountApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.

try:
    # Delete the specified robot account
    api_instance.projects_project_id_robots_robot_id_delete(project_id, robot_id)
except ApiException as e:
    print("Exception when calling RobotAccountApi->projects_project_id_robots_robot_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_get**
> projects_project_id_robots_robot_id_get(project_id, robot_id)

Return the infor of the specified robot account.

Return the infor of the specified robot account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RobotAccountApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.

try:
    # Return the infor of the specified robot account.
    api_instance.projects_project_id_robots_robot_id_get(project_id, robot_id)
except ApiException as e:
    print("Exception when calling RobotAccountApi->projects_project_id_robots_robot_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **projects_project_id_robots_robot_id_put**
> projects_project_id_robots_robot_id_put(project_id, robot_id, robot)

Update status of robot account.

Used to disable/enable a specified robot account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RobotAccountApi(swagger_client.ApiClient(configuration))
project_id = 789 # int | Relevant project ID.
robot_id = 789 # int | The ID of robot account.
robot = swagger_client.RobotAccountUpdate() # RobotAccountUpdate | Request body of enable/disable a robot account.

try:
    # Update status of robot account.
    api_instance.projects_project_id_robots_robot_id_put(project_id, robot_id, robot)
except ApiException as e:
    print("Exception when calling RobotAccountApi->projects_project_id_robots_robot_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**| Relevant project ID. | 
 **robot_id** | **int**| The ID of robot account. | 
 **robot** | [**RobotAccountUpdate**](RobotAccountUpdate.md)| Request body of enable/disable a robot account. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

