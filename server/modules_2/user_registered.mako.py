# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1502268878.1415215
_enable_loop = True
_template_filename = 'htdocs/user_registered.mako'
_template_uri = 'user_registered.mako'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'root.mako', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        username = context.get('username', UNDEFINED)
        qr_blob = context.get('qr_blob', UNDEFINED)
        totp_secret = context.get('totp_secret', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<h1>User registered</h1>\n<h2>Name</h2>\n')
        __M_writer(str(username))
        __M_writer('\n<h2>Two-factor authentication</h2>\n<p>Insert this code (')
        __M_writer(str(totp_secret))
        __M_writer(') or scan the following QR code in your two-factor authentication app (ie. Google Authenticator).</p>\n<p><img src="data:image/png;base64,')
        __M_writer(str(qr_blob))
        __M_writer('"/></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "user_registered.mako", "source_encoding": "utf-8", "filename": "htdocs/user_registered.mako", "line_map": {"35": 1, "36": 5, "37": 5, "38": 7, "39": 7, "40": 8, "41": 8, "27": 0, "47": 41}}
__M_END_METADATA
"""
