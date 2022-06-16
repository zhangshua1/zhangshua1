<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>重置密码 - ${SITE_NAME} - Powered By JEESNS</title>
    <meta name="keywords" content="${SITE_KEYS}"/>
    <meta name="description" content="${SITE_DESCRIPTION}"/>
    <meta name="author" content="JEESNS"/>
    <link rel="shortcut icon" href="favicon.ico">
    <link href="${basePath}/res/common/css/zui.min.css" rel="stylesheet">
    <link href="${basePath}/res/front/css/app.css" rel="stylesheet">
    <!--[if lt IE 9]>
    <script src="${basePath}/res/common/js/html5shiv.min.js"></script>
    <script src="${basePath}/res/common/js/respond.min.js"></script>
    <![endif]-->
    <script src="${basePath}/res/common/js/jquery-2.1.1.min.js"></script>
    <script src="${basePath}/res/common/js/zui.min.js"></script>
    <script src="${basePath}/res/plugins/layer/layer.js"></script>
    <script src="${basePath}/res/common/js/jquery.form.js"></script>
    <script src="${basePath}/res/common/js/jeesns.js?v1.4"></script>
    <script>
        var _success = function () {
            window.location.href = '${basePath}/member/login';
        }
    </script>
</head>

<body class="gray-bg">
<#include "/${frontTemplate}/common/header.ftl"/>
<div class="wrapper wrapper-content">
    <div class="container">
        <div class="row">
            <div class="col-md-3"></div>
            <div class="col-md-6 white-bg m-b-20 p-20">
                <header class="m-b-50">
                    <h1> 重置密码</h1>
                </header>
                <form class="form-horizontal jeesns_form" action="${basePath}/member/resetpwd" method="post"
                      callback="_success">
                    <input name="email" class="form-control" type="hidden" value="${email}">
                    <input name="token" class="form-control" type="hidden" value="${token}">
                    <div class="form-group m-b-30">
                        <label class="col-sm-3">新密码</label>
                        <div class="col-md-8 col-sm-10">
                            <input id="newPassword" name="password" class="form-control" type="password" data-type="require" alt="新密码">
                        </div>
                    </div>
                    <div class="form-group m-b-30">
                        <label class="col-sm-3">确认新密码</label>
                        <div class="col-md-8 col-sm-10">
                            <input id="renewPassword" name="repassword" class="form-control" type="password" data-type="require" data-rule="equal[newPassword]" alt="两次密码必须一致">
                        </div>
                    </div>
                    <div class="form-group m-b-90">
                        <label class="col-sm-3"></label>
                        <div class="col-md-8 col-sm-10">
                            <button type="submit" class="btn btn-primary btn-block m-t-10">重置密码</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
<#include "/${frontTemplate}/common/footer.ftl"/>
</body>
</html>
