<div class="col-sm-2 col-xs-12">
    <ul class="list-group">
        <li class="list-group-item"><a href="${basePath}/member/financial/list">财务明细</a></li>
        <li class="list-group-item"><a href="${basePath}/member/scoreDetail/list">积分明细</a></li>
        <#if payExists == true>
            <#if ALIPAY_OPEN == 1>
                <li class="list-group-item"><a href="${basePath}/pay/alipay/recharge">支付宝充值</a></li>
            </#if>
            <#if PAYJS_OPEN == 1>
                <li class="list-group-item"><a href="${basePath}/pay/wxpay/recharge">微信充值</a></li>
            </#if>
        </#if>
        <#if extExists == true>
              <li class="list-group-item"><a href="${basePath}/member/cdkRecharge">卡密充值</a></li>
        </#if>
        <li class="list-group-item"><a href="${basePath}/member/message">私信</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}">动态</a></li>
        <li class="list-group-item"><a href="${basePath}/member/picture/album">相册</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/fans">粉丝</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/follows">关注</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/article">文章</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/groupTopic">群帖</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/weibo">微博</a></li>
        <li class="list-group-item"><a href="${basePath}/u/${loginUser.id}/home/group">关注群组</a></li>
    </ul>
</div>