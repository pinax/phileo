from django.conf import settings  # noqa

from appconf import AppConf
from collections import defaultdict


class PinaxLikesAppConf(AppConf):

    DEFAULT_LIKE_CONFIG = {
        "css_class_on": "icon-heart",
        "css_class_off": "icon-heart-empty",
        "like_text_on": "Unlike",
        "like_text_off": "Like",
        "count_text_singular": "like",
        "count_text_plural": "likes",
    }

    LIKABLE_MODELS = getattr(settings, "PINAX_LIKES_LIKABLE_MODELS", defaultdict(dict))

    for model in LIKABLE_MODELS:
        custom_data = LIKABLE_MODELS[model].copy()
        default_data = DEFAULT_LIKE_CONFIG.copy()
        LIKABLE_MODELS[model] = default_data
        LIKABLE_MODELS[model].update(custom_data)
