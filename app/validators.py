from django.core.exceptions import ValidationError

def validate_telegram_link (val) : 
    if "web.telegram.org/k/#@" not in str(val) :
        raise ValidationError("invalid url for telegram",code=400)
    return val

def validate_whatsapp_link (val) : 
    if "wa.me" not in str(val):
        raise ValidationError('invalid url for whatsapp',code=400)
    return val

def validate_student_collage_id (val) : 
    if len(str(val)) != 10 :
        raise ValidationError('invalid student collage id',code=400)
    return val