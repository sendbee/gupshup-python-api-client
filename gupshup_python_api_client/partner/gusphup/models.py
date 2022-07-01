from gupshup_python_api_client.models import Model
from gupshup_python_api_client.fields import TextField, RealNumberField, \
    NumberField, ModelField


class Discount(Model):
    """Data model for Gupshup app discounts"""

    _cumulative_bill = NumberField(
        index='cumulativeBill', desc='Cumulative bill')
    _daily_bill = NumberField(index='dailyBill', desc='Daily bill')
    _day = NumberField(index='day', desc='Day')
    _discount = NumberField(index='discount', desc='Discount')
    _cap = NumberField(index='gsCap', desc='Gupshup cap')
    _fees = NumberField(index='gsFees', desc='Gupshup fees')


class AppDailyDiscount(Model):
    """Data model for Gupshup app discount list"""

    _discount_list = ModelField(
        Discount, index='dailyAppDiscountList',
        desc='Gupshup app discount list')


class Balance(Model):
    """Data model for Gupshup app wallet"""

    _currency = TextField(index='currency', desc='Currency')
    _current_balance = RealNumberField(
        index='currentBalance', desc='Current balance')
    _overdraft_limit = RealNumberField(
        index='overDraftLimit', desc='Overdraft limit')


class WalletBalance(Model):
    """Data model for Gupshup app wallet balance"""

    _wallet = ModelField(
        Balance, index='walletResponse',
        desc='Gupshup app wallet')
