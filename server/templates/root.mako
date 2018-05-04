<% self.seen_css = set() %>
<%def name="css_link(path, media='')" filter="trim">
    % if path not in self.seen_css:
    <link rel="stylesheet" type="text/css" href="${path|h}" media="${media}">
    % endif
    <% self.seen_css.add(path) %>
</%def>
<%def name="css()" filter="trim">
    ${css_link('/static/bootstrap/css/bootstrap.min.css', 'screen')}
    ${css_link('/static/bootstrap/css/style.css', 'screen')}
</%def>
<%def name="pre()" filter="trim">
</%def>
<%def name="post()" filter="trim">
<div>
    <div class="footer">
    </div>
</div>
</%def>
##<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN "
##"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html>
<head><title>OpenID Connect provider example</title>
${self.css()}
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<script src="/static/recorder.js"></script>
<script src="/static/main.js"></script>
</head>
<body>
${pre()}
##        ${comps.dict_to_table(pageargs)}
##        <hr><hr>
${next.body()}
${post()}
</body>
</html>