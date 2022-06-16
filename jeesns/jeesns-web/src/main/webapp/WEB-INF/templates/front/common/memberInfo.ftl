<div class="member-banner" style="background-image: url(${basePath}/res/common/images/member_banner.png);">
    <div class="attempts"></div>
    <div class="container">
        <div class="row">
            <div class="col-sm-6 col-xs-12 left">
                <div class="avatar">
                    <img src="${basePath}${member.avatar}" class="img-circle" width="100%" height="100%"/>
                </div>
                <div class="info">
                    <div class="name">
                    ${member.name}
                        <#if member.sex=='女'>
                            <span class="sex"><i class="icon icon-venus"></i></span>
                        <#elseif member.sex=='男'>
                            <span class="sex"><i class="icon icon-mars"></i></span>
                        <#else>
                            <span class="sex"><i class="icon icon-intersex"></i></span>
                        </#if>
                        <span class="label label-danger" style="font-size: 12px;">${member.memberLevel.name}</span>
                        <a class="label label-primary edit member-follows" member-id="${member.id}">
                            <i class="icon icon-heart-o"></i> 关注
                        </a>&nbsp;
                        <a class="label label-primary edit" href="javascript:void(0)" data-href="${basePath}/member/sendMessageBox?mid=${member.id}"
                           target="_jeesnsOpen" title="私信" height="285px">
                            <i class="icon icon-comments"></i> 私信
                        </a>
                    </div>
                    <p>${member.website}</p>
                    <p>${member.introduce}</p>
                </div>
            </div>
            <div class="col-sm-6 col-xs-12 right">
                <div class="follows">
                    <span>关注</span>
                    <a href="${basePath}/u/${member.id}/home/follows">${member.follows}</a>
                </div>
                <div class="fans">
                    <span>粉丝</span>
                    <a href="${basePath}/u/${member.id}/home/fans">${member.fans}</a>
                </div>
                <div class="score">
                    <span>积分</span>
                    <a href="${basePath}/member/scoreDetail/list">${member.score}</a>
                </div>
                <div class="login-info">
                    加入时间:${member.createTime?string('yyyy-MM-dd')}
                    最近登录:<#if member.currLoginTime??>${member.currLoginTime?string('yyyy-MM-dd')}<#else>未登陆过</#if>
                </div>
            </div>
        </div>
    </div>
</div>