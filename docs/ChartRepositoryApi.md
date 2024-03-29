# swagger_client.ChartRepositoryApi

All URIs are relative to *http://localhost/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartrepo_charts_post**](ChartRepositoryApi.md#chartrepo_charts_post) | **POST** /chartrepo/charts | Upload a chart file to the defult &#39;library&#39; project.
[**chartrepo_health_get**](ChartRepositoryApi.md#chartrepo_health_get) | **GET** /chartrepo/health | Check the health of chart repository service.
[**chartrepo_repo_charts_get**](ChartRepositoryApi.md#chartrepo_repo_charts_get) | **GET** /chartrepo/{repo}/charts | Get all the charts under the specified project
[**chartrepo_repo_charts_name_delete**](ChartRepositoryApi.md#chartrepo_repo_charts_name_delete) | **DELETE** /chartrepo/{repo}/charts/{name} | Delete all the versions of the specified chart
[**chartrepo_repo_charts_name_get**](ChartRepositoryApi.md#chartrepo_repo_charts_name_get) | **GET** /chartrepo/{repo}/charts/{name} | Get all the versions of the specified chart
[**chartrepo_repo_charts_name_version_delete**](ChartRepositoryApi.md#chartrepo_repo_charts_name_version_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version} | Delete the specified chart version
[**chartrepo_repo_charts_name_version_get**](ChartRepositoryApi.md#chartrepo_repo_charts_name_version_get) | **GET** /chartrepo/{repo}/charts/{name}/{version} | Get the specified chart version
[**chartrepo_repo_charts_name_version_labels_get**](ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_get) | **GET** /chartrepo/{repo}/charts/{name}/{version}/labels | Return the attahced labels of chart.
[**chartrepo_repo_charts_name_version_labels_id_delete**](ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_id_delete) | **DELETE** /chartrepo/{repo}/charts/{name}/{version}/labels/{id} | Remove label from chart.
[**chartrepo_repo_charts_name_version_labels_post**](ChartRepositoryApi.md#chartrepo_repo_charts_name_version_labels_post) | **POST** /chartrepo/{repo}/charts/{name}/{version}/labels | Mark label to chart.
[**chartrepo_repo_charts_post**](ChartRepositoryApi.md#chartrepo_repo_charts_post) | **POST** /chartrepo/{repo}/charts | Upload a chart file to the specified project.
[**chartrepo_repo_prov_post**](ChartRepositoryApi.md#chartrepo_repo_prov_post) | **POST** /chartrepo/{repo}/prov | Upload a provance file to the specified project.


# **chartrepo_charts_post**
> chartrepo_charts_post(chart, prov=prov)

Upload a chart file to the defult 'library' project.

Upload a chart file to the default 'library' project. Uploading together with the prov file at the same time is also supported.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
chart = '/path/to/file.txt' # file | The chart file
prov = '/path/to/file.txt' # file | The provance file (optional)

try:
    # Upload a chart file to the defult 'library' project.
    api_instance.chartrepo_charts_post(chart, prov=prov)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_charts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chart** | **file**| The chart file | 
 **prov** | **file**| The provance file | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_health_get**
> InlineResponse200 chartrepo_health_get()

Check the health of chart repository service.

Check the health of chart repository service.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))

try:
    # Check the health of chart repository service.
    api_response = api_instance.chartrepo_health_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_health_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_get**
> list[ChartInfoEntry] chartrepo_repo_charts_get(repo)

Get all the charts under the specified project

Get all the charts under the specified project

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name

try:
    # Get all the charts under the specified project
    api_response = api_instance.chartrepo_repo_charts_get(repo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 

### Return type

[**list[ChartInfoEntry]**](ChartInfoEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_delete**
> chartrepo_repo_charts_name_delete(repo, name)

Delete all the versions of the specified chart

Delete all the versions of the specified chart

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name

try:
    # Delete all the versions of the specified chart
    api_instance.chartrepo_repo_charts_name_delete(repo, name)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_get**
> chartrepo_repo_charts_name_get(repo, name)

Get all the versions of the specified chart

Get all the versions of the specified chart

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name

try:
    # Get all the versions of the specified chart
    api_instance.chartrepo_repo_charts_name_get(repo, name)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_delete**
> chartrepo_repo_charts_name_version_delete(repo, name, version)

Delete the specified chart version

Delete the specified chart version

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Delete the specified chart version
    api_instance.chartrepo_repo_charts_name_version_delete(repo, name, version)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_get**
> chartrepo_repo_charts_name_version_get(repo, name, version)

Get the specified chart version

Get the specified chart version

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Get the specified chart version
    api_instance.chartrepo_repo_charts_name_version_get(repo, name, version)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_get**
> chartrepo_repo_charts_name_version_labels_get(repo, name, version)

Return the attahced labels of chart.

Return the attahced labels of the specified chart version.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version

try:
    # Return the attahced labels of chart.
    api_instance.chartrepo_repo_charts_name_version_labels_get(repo, name, version)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_labels_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_id_delete**
> chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)

Remove label from chart.

Remove label from the specified chart version.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version
id = 56 # int | The label ID

try:
    # Remove label from chart.
    api_instance.chartrepo_repo_charts_name_version_labels_id_delete(repo, name, version, id)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_labels_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 
 **id** | **int**| The label ID | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_name_version_labels_post**
> chartrepo_repo_charts_name_version_labels_post(repo, name, version, label)

Mark label to chart.

Mark label to the specified chart version.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
name = 'name_example' # str | The chart name
version = 'version_example' # str | The chart version
label = swagger_client.Label() # Label | The label being marked to the chart version

try:
    # Mark label to chart.
    api_instance.chartrepo_repo_charts_name_version_labels_post(repo, name, version, label)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_name_version_labels_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **name** | **str**| The chart name | 
 **version** | **str**| The chart version | 
 **label** | [**Label**](Label.md)| The label being marked to the chart version | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_charts_post**
> chartrepo_repo_charts_post(repo, chart, prov=prov)

Upload a chart file to the specified project.

Upload a chart file to the specified project. With this API, the corresponding provance file can be uploaded together with chart file at once.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
chart = '/path/to/file.txt' # file | The chart file
prov = '/path/to/file.txt' # file | The provance file (optional)

try:
    # Upload a chart file to the specified project.
    api_instance.chartrepo_repo_charts_post(repo, chart, prov=prov)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_charts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **chart** | **file**| The chart file | 
 **prov** | **file**| The provance file | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **chartrepo_repo_prov_post**
> chartrepo_repo_prov_post(repo, prov)

Upload a provance file to the specified project.

Upload a provance file to the specified project. The provance file should be targeted for an existing chart file.

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
api_instance = swagger_client.ChartRepositoryApi(swagger_client.ApiClient(configuration))
repo = 'repo_example' # str | The project name
prov = '/path/to/file.txt' # file | The provance file

try:
    # Upload a provance file to the specified project.
    api_instance.chartrepo_repo_prov_post(repo, prov)
except ApiException as e:
    print("Exception when calling ChartRepositoryApi->chartrepo_repo_prov_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | **str**| The project name | 
 **prov** | **file**| The provance file | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

