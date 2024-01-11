# OrderCreateRequestVmf

Vendor mandatory fields, this is required in case of warranty orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vend_auth_number** | **str** | Authorization number provided by vendor to Ingram&#39;s reseller. Orders will be placed on hold without this value, vendor specific mandatory field - please reach out Ingram Sales team for list of vendor for whom this is mandatory. | [optional] 

## Example

```python
from xi-sdk-resellers-python.models.order_create_request_vmf import OrderCreateRequestVmf

# TODO update the JSON string below
json = "{}"
# create an instance of OrderCreateRequestVmf from a JSON string
order_create_request_vmf_instance = OrderCreateRequestVmf.from_json(json)
# print the JSON string representation of the object
print OrderCreateRequestVmf.to_json()

# convert the object into a dict
order_create_request_vmf_dict = order_create_request_vmf_instance.to_dict()
# create an instance of OrderCreateRequestVmf from a dict
order_create_request_vmf_form_dict = order_create_request_vmf.from_dict(order_create_request_vmf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


