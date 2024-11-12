# errors.py
class SalesPipelineError(Exception):
    """Base class for all sales pipeline related errors."""
    pass

class KickoffError(SalesPipelineError):
    """Error during the kickoff process."""
    pass

class ValidationError(SalesPipelineError):
    """Error during the validation process."""
    pass
