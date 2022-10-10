
class CPanel:

    def __init__(self, req):
        self.req = req

    def fetch_payment_session_timeout(self):
        """

        :return:
        """
        endpoint = 'integration/payment_session_timeout'
        return self.req.get(endpoint=endpoint)

    def update_payment_session_timeout(self, *, timeout):
        """

        :param timeout:
        :return:
        """
        endpoint = 'integration/payment_session_timeout'
        return self.req.put(endpoint=endpoint, json={'timeout': timeout})
