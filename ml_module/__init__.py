from ml_module.context import Context
from ml_module.policy import Policy


def create_model(criteria):
    context_object = Context()
    policy_object = Policy(context_object)
    policy_object.configure(criteria)

    return context_object
