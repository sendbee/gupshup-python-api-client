class ApiClientException(Exception):
	"""Handle All API Client Exceptions"""


class RequestApiException(ApiClientException):
	"""Handle Request Exceptions"""


class FormatterException(ApiClientException):
	"""Handle Formatter Exceptions"""


class PaginationException(ApiClientException):
	"""Handle Pagination Exceptions"""
