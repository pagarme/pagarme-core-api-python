from pagarmecoreapi.pagarmecoreapi_client import PagarmecoreapiClient
from pagarmecoreapi.models import *
from pagarmecoreapi.controllers import *
from pagarmecoreapi.exceptions.error_exception import *

# Configuration parameters and credentials
basic_auth_user_name = 'basic_auth_user_name' # The username to use with basic authentication
basic_auth_password = 'basic_auth_password' # The password to use with basic authentication

PagarmecoreapiClient(basic_auth_user_name, basic_auth_password)

orders_controller = orders_controller.OrdersController()

customer = create_customer_request.CreateCustomerRequest()
customer.name = "sdk customer test"
customer.email = "tonystark@avengers.com"

bank_transfer = create_bank_transfer_payment_request.CreateBankTransferPaymentRequest()
bank_transfer.bank = "001"

request = create_order_request.CreateOrderRequest()

request.items = [create_order_item_request.CreateOrderItemRequest()]
request.items[0].description = "Tesseract Bracelet"
request.items[0].quantity = 3
request.items[0].amount = 1490

request.payments = [create_payment_request.CreatePaymentRequest()]
request.payments[0].payment_method = "bank_transfer"
request.payments[0].bank_transfer = bank_transfer
request.customer = customer

try:
    result = orders_controller.create_order(request)
    assert result.status == "pending"
    assert result.charges[0].status == "pending"
    assert result.charges[0].last_transaction.status == "pending"
    assert result.charges[0].last_transaction.success is True
    assert result.charges[0].last_transaction.url is not None
    assert result.charges[0].last_transaction.bank_tid is not None
    assert result.charges[0].last_transaction.bank == "001"
    print("Order result status: ", result.status)
    print("Order id: ", result.id)
except ErrorException as ex:
    print(ex.message)
    print("Errors: ", ex.errors)
except Exception as ex:
    raise ex
    