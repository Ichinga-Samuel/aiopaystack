from .base import Base


class Verification(Base):
    """
    The Verification API allows you perform KYC processes
    """
    def __init__(self):
        super().__init__()
        url = "/bank/{}"
        self.url = url.format


    async def resolve_account_number(self, *, account_number: str, bank_code: str, **kwargs):
        """
        Confirm an account belongs to the right customer
        :param account_number: Account Number
        :param bank_code: You can get the list of bank codes by calling the List Bank endpoint
        :param kwargs:
        :return: Response
        """
        params = {'account_number': account_number, 'bank_code': bank_code, **kwargs}
        return await self.get(url=self.url('resolve'), params=params)

    async def validate_account(self, *, account_name: str, account_number: str, account_type: str, bank_code: str, country_code: str, document_type: str):
        """
        Confirm the authenticity of a customer's account number before sending money
        :param account_name: Customer's first and last name registered with their bank
        :param account_number: Customer's account number
        :param account_type: This can take one of: [ personal, business ]
        :param bank_code: The bank code of the customer's bank. You can fetch the bank codes by using our List Bank endpoint
        :param document_type: This could be one of: [ identityNumber, passportNumber, businessRegistrationNumber ]
        :return: Response
        """
        data = {'account_name': account_name, 'account_number': account_number, 'account_type': account_type, 'bank_code': bank_code, 'country_code': country_code, 'document_type': document_type}
        return await self.get(url=self.url('validate'), json=data)



    async def resove_card_bin (self, *, bin: str):
        """
        Get more information about a customer's card
        :param bin: First 6 characters of card
        :return: Response
        """
        params = {'bin': bin}
        return await self.get(url=self.url("bin"), param=params)

    # async def verify_card_bin(self, *, card_bin):
    #     """
    #
    #     :param card_bin:
    #     :return:
    #     """
    #     endpoint = f'decision/bin/{card_bin}'
    #     return await self.req.get(endpoint=endpoint)
    #
    # async def verify_phone_number(self, **kwargs):
    #     """
    #
    #     :param kwargs:
    #     :return:
    #     """
    #     endpoint = "verifications"
    #     return await self.req.get(endpoint=endpoint, json=kwargs)
    #
    # async def match_bvn(self, **kwargs):
    #     """
    #
    #     :param kwargs:
    #     :return:
    #     """
    #     endpoint = "bvn/match"
    #     return await self.req.get(endpoint=endpoint, json=kwargs)
