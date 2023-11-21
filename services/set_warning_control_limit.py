def result_check(upper_control_limit, lower_control_limit, target_value, value):
    return target_value + upper_control_limit >= value >= target_value + lower_control_limit


def set_upper_control_limit(upper_tolerance, percentage):
    upper_control_limit = percentage * upper_tolerance
    return upper_control_limit


def set_lower_control_limit(lower_tolerance, percentage):
    lower_control_limit = percentage * lower_tolerance
    return lower_control_limit


def set_upper_warning_limit(upper_tolerance, percentage):
    upper_warning_limit = percentage * upper_tolerance
    return upper_warning_limit


def set_lower_warning_limit(lower_tolerance, percentage):
    lower_warning_limit = percentage * lower_tolerance
    return lower_warning_limit
