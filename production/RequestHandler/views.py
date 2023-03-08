from django.shortcuts import render
from django.views.generic import TemplateView

from .exceptions import _handle_exceptions
from .functions import (
    linear_regression,
    support_vector_machine,
    artificial_neural_network,
)


class Predict(TemplateView):
    """Handles requests to root endpoint.

    Returns:
        HttpResponse: Initial template, prediction respone or error message
    """

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["models"] = [
            ["lr", "Linear Regression"],
            ["svm", "Support Vector Machine (SVM)"],
            ["ann", "Artificial Neural Network (ANN)"],
        ]
        return context

    def post(self, request, *args, **kwargs):
        try:
            # index request parameters
            data = request.POST.get("data")
            model = request.POST.get("model")

            # sanitize input
            _handle_exceptions(data)

            # forward data to respective model
            _, pred = switch[model](int(data))

            # return response
            return render(
                request,
                "home.html",
                {
                    "input": data,
                    "pred": round(pred[0], 2),
                    "models": [
                        ["lr", "Linear Regression"],
                        ["svm", "Support Vector Machine (SVM)"],
                        ["ann", "Artificial Neural Network (ANN)"],
                    ],
                },
            )

        # in the case of an error
        except Exception as error:

            # return error response
            return render(
                request,
                "home.html",
                {
                    "input": data,
                    "error": str(error),
                    "models": [
                        ["lr", "Linear Regression"],
                        ["svm", "Support Vector Machine (SVM)"],
                        ["ann", "Artificial Neural Network (ANN)"],
                    ],
                },
            )


# model routing with dictionary-embedded functions
switch = {
    "lr": linear_regression,
    "svm": support_vector_machine,
    "ann": artificial_neural_network,
}
