from .models import AvailableFeatures


def add_variable_to_context(request):
    feature = []
    for i in AvailableFeatures.objects.filter(current_status=True):
        feature.append(i.feature_name)

    return {
        'avail': feature
    }
