"""Simplified Chinese legal pages (/zh/privacy.html, /zh/terms.html), 16/10/2026.

Only the apps that speak Chinese (Drip, Kover, Grain, Tiller) are covered; the rest of the site has no Chinese tree, so
these two pages link back to the English home and the English policy, which prevails. Translated from
gen_legal_copy.py: when a Drip, Kover, Grain or Tiller section (or the purchases paragraph, or the terms) changes there,
change it here too. Built with gen_site's chrome; run `python3 tools/gen_site.py`, which calls build_zh().
"""
import gen_site as g
from gen_site import head, header, footer, write, legal_main

g.UI['zh'] = dict(g.UI['en'], skip='跳到正文', nav_apps='应用', nav_phil='理念', nav_work='合作', nav_studio='工作室',
                  lang_label='语言', nav_cta='联系我们', footer_tag='Apps for a brighter tomorrow.',
                  copyright='© 2026 Seize Apps · Izotz Cristobal Mota &amp; Sendoa Sola · 西班牙巴斯克地区',
                  footer_privacy='隐私', footer_terms='条款', toc_title='本页内容')
g.OG_LOCALE['zh'] = 'zh_CN'

PRIVACY_TITLE = '隐私政策 — Seize Apps'
PRIVACY_DESC = 'Seize 应用如何处理你的数据：没有账户，不做数据分析，内容只存放在你的设备和你自己的 iCloud 中。适用于 Drip、Kover、Grain 和 Tiller。'
TERMS_TITLE = '使用条款 — Seize Apps'
TERMS_DESC = 'Seize Apps 发布的应用的使用条款。'

PRIVACY = '''
  <p class="eyebrow">法律信息</p>
  <h1>隐私政策</h1>
  <p class="effective">自 2026 年 10 月 30 日起生效</p>
  <nav class="toc" aria-label="应用">
    <a href="#drip">Drip</a><a href="#kover">Kover</a><a href="#grain">Grain</a><a href="#tiller">Tiller</a>
  </nav>

  <p><strong>关于本页：</strong>这是 Seize Apps 隐私政策的中文版，只包含提供中文界面的应用：<a href="#drip">Drip</a>、<a href="#kover">Kover</a>、<a href="#grain">Grain</a> 和 <a href="#tiller">Tiller</a>。其他应用请见<a href="../privacy.html">英文版完整政策</a>。中文版为译文，如与英文版有不一致之处，以英文版为准。</p>

  <p><strong>简要说明：</strong>Drip、Kover、Grain 和 Tiller 设计为不需要你的数据也能正常使用。这四款应用没有用户账户，不使用广告 SDK，我们也不出售或分享任何数据。当你在 Drip、Kover、Grain 或 Tiller 中购买内容时，Apple 会告知我们这笔购买，其中不包含你的姓名或电子邮件（见<a href="#purchases">购买</a>）。你在应用中输入的内容只存放在你的设备和你自己的 iCloud 中，除非下文对该应用另有说明。</p>

  <p><strong>Tiller 另有一点：</strong>它会向 Seize 的服务器（Supabase）发送我们自己的匿名使用统计（应用的哪些部分被使用，从不包括你的体重、饮食、热量和营养素目标或你的目标，只带一个为本次安装生成的随机数字，不含任何关于你身份的信息），除非你关闭它们，请阅读<a href="#tiller">下文的说明</a>。</p>

  <h2>我们是谁</h2>
  <p>Seize Apps 是由 <strong>Izotz Cristobal Mota</strong> 和 <strong>Sendoa Sola</strong> 在西班牙巴斯克地区经营的独立应用工作室（以下称“我们”）。本页涵盖的四款应用 Drip、Kover、Grain 和 Tiller 通过 Apple App Store 和 TestFlight 分发，由 <strong>Sendoa Sola</strong> 发布，他是这四款应用的数据控制者。各应用的说明与一般说明不同时，以该应用的说明为准。</p>

  <h2>我们收集什么</h2>
  <p><strong>默认情况下，什么都不收集。</strong>这些应用不需要账户，不包含广告或跟踪 SDK，也不会把你创建的内容传给我们。我们看不到你的订阅和支出、小票、饮食记录，也看不到你在 Seize 应用中创建的任何其他内容。Tiller 还会向我们发送我们自己的匿名使用统计，除非你关闭它们（见<a href="#tiller">Tiller</a>）。</p>
  <p>购买完全由 Apple 处理。应用通过你设备上的 Apple StoreKit 核实“Pro”一次性解锁，只记住它是否有效；我们看不到是谁购买的。我们会从 Apple 的 App Store Connect 收到汇总的匿名销售和崩溃统计（例如各国的下载量），其中不含任何个人标识。</p>
  <p id="purchases"><strong>购买。</strong>当你在 Drip、Kover、Grain 或 Tiller 中购买内容（打赏、“Pro” 或解锁）、开始试用或兑换代码时，Apple 会通知我们，之后的续订和退款也会通知：哪件商品、什么时间、哪个国家或地区的 App Store、价格和币种，以及若干交易编号和 Apple 为每个账户、每款应用分别生成的一个假名标识。其中不包含你的姓名、电子邮件或 Apple ID。我们把这些信息保存在我们自己的服务器上，只用于记账以及处理退款或与购买有关的问题。我们不与任何人分享这些信息，也不用于广告或分析。我们保存六年，这是法律对会计记录要求的期限（法律依据：履行我们的法定会计义务，以及我们处理问题和退款的正当利益）。</p>

  <h2>你的数据存放在哪里</h2>
  <ul>
    <li><strong>在你的设备上。</strong>应用内容存放在本地，即应用的私有容器中（带小组件的应用，还有一个只有该应用和它自己的小组件能读取的共享 App Group 容器）。</li>
    <li><strong>在你的 iCloud 中。</strong>应用通过你个人的 iCloud 账户同步，适用 Apple 的条款，除非你在设置中关闭同步；我们无法访问你的 iCloud。</li>
  </ul>

  <h2>各应用详情</h2>

  <section id="drip">
  <h3>Drip</h3>
  <p>Drip 把你记录的服务（名称、费用、扣费周期、付款日期、类别、标签、备注和付款方式名称）<strong>存放在你的设备上</strong>，在一个只与 Drip 自己的主屏幕和锁定屏幕小组件以及它的 Siri 快捷指令共享的私有 App Group 容器中。Drip 没有账户系统，不做数据分析，也没有任何接收你数据的第三方代码。它提供两种可选购买：一次性的“Drip Pro”解锁，开启应用的额外功能（Apple 在你的设备上核实你的购买资格，包括通过家人共享获得的；应用只保存它是否有效），以及不解锁任何东西、也不改变应用任何地方的一次性打赏。两者都由 Apple 处理；我们从不接触你的付款信息，应用除了这个本地标记和你打赏次数的本地计数外，不保存任何相关信息。Apple 就每笔购买告诉我们的内容见<a href="#purchases">购买</a>。</p>
  <p><strong>iCloud 同步</strong>默认开启：你的服务会通过你个人的 iCloud 账户在你的设备之间同步，适用 Apple 的条款；我们无法访问。在设置中关闭后，数据只保存在本设备上。付款提醒和每周摘要是在你设备上安排的本地通知。</p>
  <p><em>由 Sendoa Sola 在 App Store 上发布。</em></p>
  </section>

  <section id="kover">
  <h3>Kover</h3>
  <p>Kover 把你添加的商品（名称、类别、商店、购买日期和金额、国家或地区、保修日期、序列号、售后联系方式、备注和小票照片）<strong>存放在你的设备上</strong>，在应用的私有容器中。Kover 没有账户系统，不做数据分析，也没有任何接收你数据的第三方代码。它提供两种可选购买：一次性的“Kover Pro”解锁，开启应用的额外功能（Apple 在你的设备上核实你的购买资格，包括通过家人共享获得的；应用只保存它是否有效），以及不解锁任何东西、也不改变应用任何地方的一次性打赏。两者都由 Apple 处理；我们从不接触你的付款信息，应用除了这个本地标记和你打赏次数的本地计数外，不保存任何相关信息。Apple 就每笔购买告诉我们的内容见<a href="#purchases">购买</a>。</p>
  <p><strong>小票和相机。</strong>扫描小票时，Kover 使用相机（或你选择的照片或 PDF），并用 Apple 设备端的 Vision 框架识别文字。图片和识别出的文字从不离开手机；保留照片只是因为它是你的购买凭证。只有在你使用这些功能时，才会请求相机和照片图库的访问权限。</p>
  <p><strong>iCloud 同步</strong>默认开启，你的商品和小票照片会通过你个人的 iCloud 账户在你的设备之间同步，适用 Apple 的条款；我们无法访问。在设置中关闭后，数据只保存在本设备上。保修提醒是在你设备上安排的本地通知。CSV 导出和每件商品的 PDF 是你自己创建并自行分享的文件。</p>
  <p><em>由 Sendoa Sola 在 App Store 上发布。</em></p>
  </section>

  <section id="grain">
  <h3>Grain</h3>
  <p>Grain 把你记录的内容（每种食物及其餐次、日期、克数和从来源复制的营养数值）、你的每日目标，以及你创建、修改或扫描的食物和食谱<strong>存放在你的设备上</strong>，在应用的私有容器和一个只与 Grain 自己的小组件共享的私有 App Group 容器中。Grain 没有账户系统，不做数据分析，也没有任何接收你数据的第三方代码。它提供可选购买：一次性的“Grain Pro”解锁，开启应用的额外功能，每个 Apple ID 可享一次 30 天免费试用（Apple 在你的设备上核实你的购买资格，包括通过家人共享获得的；应用只保存它是否有效，以及试用期间的结束时间），以及不解锁任何东西、也不改变应用任何地方的一次性打赏。这些都由 Apple 处理；我们从不接触你的付款信息，应用除了这个本地标记和你打赏次数的本地计数外，不保存任何相关信息。Apple 就每笔购买告诉我们的内容见<a href="#purchases">购买</a>。</p>
  <p><strong>条形码和 Open Food Facts。</strong>食物库随应用内置，在设备上搜索。当你扫描或输入一个不在你自己食物中的条形码时，Grain 只把这个号码发送给 Open Food Facts（openfoodfacts.org，一个开放的非营利食品数据库）来查询该商品；请求中只标明应用，不标明你本人，也不会发送你的任何饮食记录。Open Food Facts 按其自己的条款处理该请求。</p>
  <p><strong>向 Open Food Facts 提交商品。</strong>保存带条形码的食物时，“同时发送到 Open Food Facts”默认开启，并显示在同一表单上；你可以关闭它，Grain 会记住你的选择。开启时，Grain 会通过 Grain 自己的 Open Food Facts 账户发送该商品（条形码和每 100 克的数值，商品在 Open Food Facts 上是新的时还包括名称和品牌），并附带一个为本次安装生成的随机标识，以便其审核人员区分不同的提交。你的饮食记录、目标和 Apple 账户中的任何信息都不会发送。你发送的内容会按《开放数据库许可证》（ODbL）在该网站公开，任何人都可以使用，Grain 无法撤回；Open Food Facts 按其自己的条款处理。</p>
  <p><strong>相机、营养成分表和文字。</strong>只有在你扫描条形码或拍摄营养成分表时才使用相机，且不会保存任何画面。营养成分表（来自相机或你选择的照片）由 Apple 设备端的 Vision 框架识别；你用文字描述的一餐在 iPhone 上解析（在可用时使用 Apple 智能）。图片和文字都不会离开手机。</p>
  <p><strong>Apple 健康。</strong>默认关闭。如果你在设置中开启，每条记录会作为食物（能量、蛋白质、碳水化合物和脂肪）写入“健康”，你在 Grain 中修改或删除时，“健康”中的记录也会随之修改或删除。Grain 从不读取“健康”中的任何内容，也从不上传健康数据；权限和这一偏好只保存在该设备上。</p>
  <p><strong>iCloud 同步</strong>默认开启，你的饮食记录、目标和食物会通过你个人的 iCloud 账户在你的设备之间同步，适用 Apple 的条款；我们无法访问。在设置中关闭后，数据只保存在本设备上。Grain 不发送任何通知。</p>
  <p><em>由 Sendoa Sola 在 App Store 上发布。</em></p>
  </section>

  <section id="tiller">
  <h3>Tiller</h3>
  <p>Tiller 是一款运动营养应用：它根据你的个人信息、目标和训练计算热量和宏量营养素目标，并每周根据你的饮食和体重记录重新调整。Tiller 没有账户系统，没有自己的服务器，没有广告，也不做跟踪，没有任何接收你数据的第三方代码。它唯一发送给我们的，是下文说明的匿名使用统计；这是我们自己的统计，你可以关闭。</p>
  <p><strong>你输入的内容。</strong>你的个人资料（性别、出生年份、身高、体重、体脂率（如果你填写）、活动水平、训练课、目标和速度、每天餐数、一项计划中的赛事，以及肌酸开关）、你手动输入的称重记录和你应用的目标，保存在你的设备上，并通过你个人的 iCloud 账户（iCloud 键值存储）同步，适用 Apple 的条款；我们无法访问。这些内容都不会发送给 Seize。</p>
  <p><strong>Apple 健康。</strong>只有在你允许后，Tiller 才会从“健康”读取其他应用记录的食物能量和宏量营养素、体重、体脂率、瘦体重、身高、出生日期和生理性别。这些数据只在设备上用于计算和调整你的目标；它们从不离开设备，也从不写入 iCloud。如果你允许，Tiller 还会把你在应用中输入的称重记录写入“健康”。Tiller 从不上传健康数据。</p>
  <p><strong>Grain。</strong>如果你安装了同样来自 Seize 的 Grain，Tiller 会读取 Grain 留在设备上的每日摘要（每天的能量、宏量营养素，以及有记录的餐数）。摘要只留在设备上，Tiller 不会打开 Grain 自己的数据。</p>
  <p><strong>购买。</strong>Tiller 提供可选的一次性“Tiller Pro”解锁，开启应用的额外功能，并提供 30 天免费试用。购买由 Apple 处理，Apple 在你的设备上核实你的购买资格；我们从不接触你的付款信息。Apple 就每笔购买告诉我们的内容见<a href="#purchases">购买</a>。</p>
  <p><strong>使用统计。</strong>为了决定改进什么，Tiller 会统计它的使用情况（Seize Analytics，我们自己的代码，不是第三方 SDK）。它会在“今天”页面用一条提示和一个“好”按钮告诉你一次；此后，除非你在设置中关闭“帮助改进 Tiller”，它会发送：每个标签页在屏幕上停留多久（不计后台时间）；你看到了哪些购买页面；你何时应用目标；你接受还是推迟每周回顾；以及你输入的每次称重、你计划的每项赛事，以及你何时打开或关闭肌酸开关。从不发送你的体重、你吃的食物、你的热量和营养素目标或你的目标。随统计一起发送的有应用版本、语言、地区设置、设备类型，以及应用来自 App Store、TestFlight 还是开发版本。统计带有一个为本次安装生成的随机数字（不是你的姓名、你的 Apple 账户，也不是设备标识），我们也不保存你的 IP 地址。统计发送到我们在 Supabase（我们的数据处理者）的服务器，位于欧盟的法兰克福，最多保存 30 天；我们在自己的系统中最多保留 13 个月。我们只用它们来决定改进什么：它们不与你的身份关联，也不用于跟踪你或投放广告。关闭该设置会删除这台设备已发送的内容。</p>
  <p>Tiller 不是医疗器械，不能代替营养师或医生。有关 Tiller 和你的数据的问题：<a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a>。</p>
  <p><em>开发中；由 Sendoa Sola 发布。</em></p>
  </section>

  <h2>通知</h2>
  <p>会提醒你的应用使用本地通知，在你的设备上安排和推送。这些功能不使用我们运营的推送通知服务器。</p>

  <h2>你的权利</h2>
  <p>由于你的数据存放在你的设备上，你可以直接行使你的权利：在应用中删除内容即会删除它；删除应用会删除它的容器；关闭 iCloud 同步并删除应用，也会把数据从 iCloud 中移除（或在“设置”›“Apple 账户”›“iCloud”中管理）。根据欧盟《通用数据保护条例》（GDPR），你还享有访问权、更正权、删除权和数据可携带权。由于我们不持有你的个人数据，通常没有可以提供的内容，但你随时可以通过 <a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a> 向我们提出问题或请求。购买通知（见<a href="#purchases">购买</a>）不含姓名或电子邮件：要找到某笔购买的记录，我们需要它的订单号，就在 Apple 发给你的收据上。</p>

  <h2>未成年人</h2>
  <p>我们的应用是面向大众的实用工具，不会有意收集任何人（包括儿童）的个人信息。</p>

  <h2>变更</h2>
  <p>如果未来的应用或功能改变了上述任何内容（例如某款应用增加了在线服务），我们会在该功能上线前更新本政策和该应用在 App Store 上的隐私标签。</p>

  <h2>联系方式</h2>
  <p>Seize Apps · Izotz Cristobal Mota &amp; Sendoa Sola<br><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
'''

TERMS = '''
  <p class="eyebrow">法律信息</p>
  <h1>使用条款</h1>
  <p class="effective">自 2026 年 10 月 6 日起生效</p>

  <p><strong>关于本页：</strong>这是 Seize Apps 使用条款的中文译文。如与<a href="../terms.html">英文版</a>有不一致之处，以英文版为准。</p>

  <h2>1. 协议</h2>
  <p>本条款适用于你使用 Izotz Cristobal Mota 和 Sendoa Sola（西班牙巴斯克地区，以下称“我们”）以 Seize Apps 名义发布的应用。每款应用的销售方是其 App Store 页面上显示的开发者。应用通过 Apple App Store 和 TestFlight 分发。下载或使用 Seize 应用，即表示你同意本条款以及 Apple 的标准<a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">许可应用程序最终用户许可协议</a>，后者适用于本条款未涵盖的事项。Garum 有账户和用户内容，因此有<a href="../garum/terms/">自己的使用条款</a>，Garum 适用该条款而非本条款。</p>

  <h2>2. 许可</h2>
  <p>在 App Store 条款允许的范围内，我们授予你在你拥有或控制的 Apple 设备上使用我们应用的个人、非独占、不可转让的许可。应用及其设计和代码仍归我们所有。</p>

  <h2>3. 购买</h2>
  <p>付费应用和 App 内购买由 Apple 按你确认前 App Store 中显示的价格收费。订阅在每个周期结束时以相同价格自动续订，除非你在周期结束前至少 24 小时在 Apple 账户设置中取消，你也可以随时在那里管理订阅。退款由 Apple 按 App Store 的退款政策处理，我们无法直接退款。</p>

  <h2>4. 你的内容归你所有</h2>
  <p>你在 Seize 应用中创建的任何内容（计时器、工作记录、支出、日常安排、小票、训练日志、饮食记录）都归你所有。正如我们的<a href="../privacy.html">隐私政策</a>（英文版完整政策；Drip、Kover 和 Grain 另见<a href="privacy.html">中文版</a>）所述，这些内容存放在你的设备和你自己的 iCloud 中，我们无法访问，这也意味着<strong>你需要自行负责备份</strong>。唯一的例外是你从 Grain 发送到 Open Food Facts 的商品，它会按《开放数据库许可证》在该网站公开。删除应用会删除它在该设备上的数据；你 iCloud 中的内容会一直保留，直到你在那里删除。</p>

  <h2>5. 不构成专业建议</h2>
  <p>我们的应用是整理工具，不构成医疗、营养、心理、财务或法律建议。我们任何涉及身心健康的应用都只是辅助陪伴，<strong>不能替代专业治疗</strong>；如果你正处于困境，请寻求专业人士的帮助。Kover 显示的保修期限是参考性的默认值；你的权利取决于每笔购买适用的法律和商家条款。</p>

  <h2>6. 合理使用</h2>
  <p>不得对应用进行逆向工程、转售或滥用，也不得以任何违反法律或 Apple 条款的方式使用。</p>

  <h2>7. 担保与责任</h2>
  <p>应用按“现状”提供，不附带任何形式的担保。在法律允许的最大范围内，我们不对因使用应用而产生的间接或后果性损害承担责任；我们的总责任以你在提出索赔前十二个月内为该应用支付的金额为限。本条款不限制消费者保护法律赋予你且不可放弃的权利。</p>

  <h2>8. 变更</h2>
  <p>随着应用的发展，我们可能会更新本条款；当前版本始终在此地址，生效日期见上方。变更后继续使用即表示你接受更新后的条款。</p>

  <h2>9. 适用法律</h2>
  <p>本条款受西班牙法律管辖。欧盟的消费者还保留其居住国法律提供的保护。</p>

  <h2>联系方式</h2>
  <p><a href="mailto:hello@seizeapps.com">hello@seizeapps.com</a></p>
'''


def _chrome(html):
    # There is no Chinese home: the header and footer point at the English one, and the page says zh-Hans.
    # The language switch only lists the site's languages: add 中文 as the current one.
    return (html.replace('href="../zh/index.html', 'href="../index.html').replace('<html lang="zh">', '<html lang="zh-Hans">')
            .replace('>FR</a></div>', '>FR</a><span aria-current="true" lang="zh-Hans">中文</span></div>', 1))


# Chinese headings have no ASCII to slug: give legal_main the ids of the English pages instead.
SLUGS = {'我们是谁': 'who-we-are', '我们收集什么': 'what-we-collect', '你的数据存放在哪里': 'where-your-data-lives',
         '各应用详情': 'per-app-details', '通知': 'notifications', '你的权利': 'your-rights', '未成年人': 'children',
         '变更': 'changes', '联系方式': 'contact', '1. 协议': '1-agreement', '2. 许可': '2-license', '3. 购买': '3-purchases',
         '4. 你的内容归你所有': '4-your-content-stays-yours', '5. 不构成专业建议': '5-not-professional-advice',
         '6. 合理使用': '6-acceptable-use', '7. 担保与责任': '7-warranty-and-liability', '8. 变更': '8-changes',
         '9. 适用法律': '9-governing-law'}


def build_zh():
    root = '../'
    ascii_anchor = g.anchor
    g.anchor = lambda s: SLUGS.get(g.plain(s)) or ascii_anchor(s)
    for kind, title, desc, body in (('privacy', PRIVACY_TITLE, PRIVACY_DESC, PRIVACY),
                                    ('terms', TERMS_TITLE, TERMS_DESC, TERMS)):
        path = f'zh/{kind}.html'
        # Only these two pages exist in Chinese and they cover fewer apps: no hreflang (a Chinese browser is not sent
        # here from the full policy); the switch goes to the full page in each language.
        alts = {'zh': f'https://seizeapps.com/{path}'}
        switch = {L: f'{root}{g.prefix(L)}{kind}.html' for L in g.LANGS}
        html = (head('zh', title, desc, root, path, alts=alts) + header('zh', root, path, switch=switch)
                + legal_main('zh', body) + footer('zh', root))
        write(path, _chrome(html))
    g.anchor = ascii_anchor
