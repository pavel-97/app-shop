from datetime import date


def get_path(instance, filename):
    format_img = filename.split('.')[-1]
    loaded_at = date.today().strftime('%d-%m-%Y')
    return 'app_profile/{}/{}.{}'.format(
        instance.user.username,
        loaded_at,
        format_img)