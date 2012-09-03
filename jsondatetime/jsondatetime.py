import simplejson as json
import datetime

DEFAULT_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S UTC'
DEFAULT_ARGUMENT = "datetime_format"

def loads(s, **kwargs):

    format = kwargs.pop(DEFAULT_ARGUMENT, None) or DEFAULT_DATE_FORMAT

    source = json.loads(s, **kwargs)

    for k, v in source.items():
        if isinstance(v, basestring):
            try:
                source[k] = datetime.datetime.strptime(v, format)
            except:
                pass

    return source
