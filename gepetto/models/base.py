import abc

class LanguageModel(abc.ABC):
    @abc.abstractmethod
    def query_model_async(self, query, cb):
        pass

def get_model(model, *args, **kwargs):
    """
    Instantiates a model based on its name
    :param model:
    :return:
    """
    if model not in ["gpt-3.5-turbo", "gpt-4"]:
        raise ValueError(f"Fatal error: {model} does not exist!")
    from gepetto.models.openai import GPT
    return GPT(model)
