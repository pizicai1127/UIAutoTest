# 一 介绍



# 为什么选择Playwright

Playwright能够跨越所有现代浏览器实现快速、可靠和功能强大的测试和自动化工作。本指南涵盖了这些关键的区别点，以帮助您为自动化测试选择正确的工具。



## 支持所有浏览器

- 在Chromium、Firefox和WebKit上进行测试：Playwright的API覆盖了所有现代浏览器，包括谷歌Chrome和微软Edge（Chrome内核）、苹果Safari（WebKit内核）和Mozilla Firefox；
- 跨平台WebKit测试：通过Playwright，使用针对Windows、Linux和macOS的WebKit版本，测试应用程序在Apple Safari中的表现，支持在本地和CI环境下运行测试；
- 模拟移动端测试：使用Playwithr提供的设备仿真功能，测试web应用程序在移动端浏览器中的表现；
- 支持浏览器无头和有头模式：Playwright支持所有浏览器和所有平台的无头（无浏览器用户界面）和有头（有浏览器用户界面）模式。有头模式非常适合调试，而无头模式速度更快，适合CI/云执行；



## 快速可靠的执行

- 内置支持自动等待操作元素就绪的API，这提高了测试可靠性并简化了测试用例编写；
- Playwright接收浏览器信号，如网络请求、页面导航和页面加载事件，消除在用例中使用硬编码的方式来设置最大超时时间；
- 与浏览器上下文快速隔离：对具有浏览器上下文的多个独立执行环境重用单个浏览器实例；
- 弹性的页面元素选择器：Playwright可以依靠面向用户的字符串，如文本内容和label标签来选择元素，这些字符串往往比紧密耦合到DOM结构的选择器更有弹性。



## 强大的自动化能力

- 支持处理多个域、多页面和多frame的场景：Playwright是一个进程外自动化驱动程序，它不受页面内JavaScript执行范围的限制；
- 强大的网络控制能力：Playwright将上下文范围的网络拦截引入存根以及模拟网络请求；
- 支持现代化的网络特性：Playwright通过shadow-piercing selectors、geolocation、permissions、web workers和其他web API来支持web组件；
- 覆盖所有场景的能力：支持文件下载和上载、进程外iFrame、本地输入事件，甚至是黑暗模式；



# 快速开始

## 安装

> 系统要求
>
> Python3.7 或以上

### Pip

```shell
pip install --upgrade pip
pip install playwright
playwright install
```

### Conda

```shell
conda config --add channels conda-forge
conda config --add channels microsoft
conda install playwright
playwright install
```

注意：`playwright install` 命令会安装Chromium、Firefox和WebKit三种的浏览器的二进制安装包，要修改此行为，请参见<a href="#installBrowsers">安装参数部分的内容</a>。



## 用法

安装Playwright库后，可以在Python脚本中导入，并启动3种浏览器（chromium、firefox和webkit）中的任意一种。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://playwright.dev")
    print(page.title())
    browser.close()
```

Playwright支持同步和异步API。如果您的项目使用asyncio（异步），则应使用async API：

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())
```





### First script

在第一个脚本中，我们将导航到whatsmyuseragent.org页面，并在WebKit中截图。

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
```

在默认情况下，playwright以无头模式运行浏览器，若要查看浏览器界面，需要在启动浏览器时传递headless=False参数。您还可以传入`slow_mo`参数来降低执行速度，这一部分的内容将会在调试工具部分进行详细介绍。

```python
firefox.launch(headless=False, slow_mo=50)
```



### 录制脚本

Playwright提供了可用于记录用户交互，并自动生成Python代码的命令行接口。

```shell
playwright codegen wikipedia.org
```





### 结合Pytest

有关Pytest说明和示例，后续有专门的章节进行介绍。

### 交互模式（解释器模式）

直接通过终端 执行脚本 ，不通过解析器（同步）



```bash
python
```

```py
>>> from playwright.sync_api import sync_playwright
>>> playwright = sync_playwright().start()
# Use playwright.chromium, playwright.firefox or playwright.webkit
# Pass headless=False to launch() to see the browser UI
>>> browser = playwright.chromium.launch()
>>> page = browser.new_page()
>>> page.goto("http://whatsmyuseragent.org/")
>>> page.screenshot(path="example.png")
>>> browser.close()
>>> playwright.stop()
```

直接通过终端执行脚本， 不通过解析器（异步

```bash
python -m asyncio
```

```py
>>> from playwright.async_api import async_playwright
>>> playwright = await async_playwright().start()
>>> browser = await playwright.chromium.launch()
>>> page = await browser.new_page()
>>> await page.goto("http://whatsmyuseragent.org/")
>>> await page.screenshot(path="example.png")
>>> await browser.close()
>>> await playwright.stop()
```



### Pyinstaller 

PyInstaller在 Windows、GNU/Linux、Mac OS X、FreeBSD、Solaris 和 AIX 下将 Python 应用程序冻结（打包）为独立的可执行文件。

您可以使用Playwright和Pyinstaller来创建独立的可执行文件。

```python
# main.py
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://whatsmyuseragent.org/")
    page.screenshot(path="example.png")
    browser.close()
```

如果要将浏览器与可执行文件捆绑在一起：

```python
# Linux/macOS
PLAYWRIGHT_BROWSERS_PATH=0 playwright install chromium
pyinstaller -F main.py

# Windows with cmd.exe
set PLAYWRIGHT_BROWSERS_PATH=0
playwright install chromium
pyinstaller -F main.py

# Windows with PowerShell
$env:PLAYWRIGHT_BROWSERS_PATH="0"
playwright install chromium
pyinstaller -F main.py
```

> 将浏览器与可执行文件捆绑在一起将生成更大的二进制文件，建议仅捆绑您使用的浏览器。

从 PyPI 安装 PyInstaller：

```
pip install pyinstaller
```

转到您的程序目录并运行：

```
pyinstaller yourprogram.py
```

Pyinstaller 使用简单操作教程：http://c.biancheng.net/view/2690.html



### 已知问题

#### 使用time.sleep() 会导致过时状态

您应该使用`page.wait_for_timeout(5000)`而不是`time.sleep(5)`，最好不要等待超时，但有时它对调试很有用。在这些情况下，Playwright源码中使用的等待方法并不是`time`模块，这是因为我们内部依赖于异步操作，当使用`time.sleep(5)`时，它们无法得到正确的处理。





### <span id="system">系统要求</span>

Playwright需要Python 3.7或更高版本，以及可跨系统运行的Chromium、Firefox以及WebKit浏览器的二进制安装包。

**Windows**

适用于Windows和Windows Linux子系统（WSL）。

**macOS**

系统版本10.14 (Mojave) 以上。

**Linux**

根据不同的Linux发行版本，可能需要安装额外的依赖项来运行浏览器。



# 调试工具

Playwright脚本使用现有的调试工具，如Node.js调试器和浏览器开发者工具。除此之外，Playwright还为浏览器自动化引入了新的调试功能。



## Playwright Inspector

Playwright Inspector是一个GUI工具，帮助编写和调试Playwright脚本，这也是默认推荐的脚本debug工具。在后文中会有章节进行详细介绍。

 ![Playwright Inspector](https://tva1.sinaimg.cn/large/008i3skNgy1gu6v6qwe69j60g90iaq5602.jpg)



## Playwright Trace Viewer

Playwright Trace Viewer是一个GUI工具，用于帮助记录脚本运行时的产生的详细堆栈信息。在后文中会有章节进行详细介绍。

![](https://tva1.sinaimg.cn/large/008i3skNgy1gu75b3pcy1j60z00gcwgn02.jpg)

## 以有头方式启动浏览器

默认情况下，Playwright以无头模式运行浏览器。要更改此行为，请传入 headless=false 作为启动选项。您还可以使用slow_mo选项来降低执行速度，并在调试时进行跟踪。

```python
# sync
chromium.launch(headless=False, slow_mo=100) # or firefox, webkit

#async
await chromium.launch(headless=False, slow_mo=100) # or firefox, webkit
```



## 浏览器开发者工具

在以有头模式运行Playwright脚本时，可以在Chromium、Firefox和WebKit中使用F12打开浏览器开发者工具。使用浏览器开发者工具有助于：

-   检查DOM树并查找元素选择器；

-   在执行期间查看控制台日志（或了解如何[通过API读取日志](https://playwright.dev/python/docs/verification#console-logs)）；

-   检查网络活动或使用其他开发者工具功能；

使用`page.pause`方法是在开发者工具中暂停Playwright脚本执行和检查页面的一种简单方法。它还将打开Playwright Inspector以帮助调试。

对于Chromium浏览器，还可以通过启动选项自动打开开发者工具：

```python
# sync
chromium.launch(devtools=True)

# async
await chromium.launch(devtools=True)
```

>   对于WebKit：在执行期间启动WebKit Inspector将阻止playwright脚本进一步执行。



## 以debug模式运行

可以通过设置`PWDEBUG` 环境变量的方式，让Playwright脚本以debug方式运行。

设置 PWDEBUG=1，将自动打开Playwright Inspector。

设置 PWDEBUG=console 将在开发者工具控制台中配置用于调试的浏览器，其具有以下特点：

-   浏览器将始终以有头模式启动；

-   将Playwright语句**默认**的超时设置为0（也就是不超时）； 

    >   补充：如果在代码中手动设置了超时时间，如：page.set_default_timeout(30000)，则调试模式下仍然会生效，将会导致运行超时。

-   在浏览器页面中配置Playwright对象，并高亮显示Playwright选择器，可用于验证文本或复合选择器；

```shell
# Linux/macOS
PWDEBUG=console pytest -s

# Windows with cmd.exe
set PWDEBUG=console
pytest -s

# Windows with PowerShell
$env:PWDEBUG="console"
pytest -s
```



## 开发者工具控制台中的选择器

当设置 PWDEBUG=console 以debug模式运行脚本时，在开发者工具控制台中将会有一个`playwright`对象可用，详细的操作步骤如下：

1.   使用PWDEBUG=console运行Playwright脚本；

2.   设置断点以暂停执行；

3.   在浏览器开发者工具中打开控制台面板；

4.   使用Playwighr API

     -   playwright.$(selector)

         根据selector，查询匹配的页面元素；

     -   playwright.$$(selector)

         和 playwright.$(selector) 类似，但是会返回所有匹配的元素（数组形式）；![](https://tva1.sinaimg.cn/large/008i3skNgy1gu6zydl7c0j60ql09z40602.jpg)

     -   playwright.inspect(selector)

     ​	在 Elements 面板显示此元素（如果相应浏览器的DevTools支持它）；

     -   playwright.selector(element)

         为给定元素生成选择器。

## 控制台打印详细的API日志

Playwright支持通过设置环境变量的方式，在运行脚本时打印详细的API日志。

```shell
# Linux/macOS
DEBUG=pw:api pytest -s

# Windows with cmd.exe
set DEBUG=pw:api
pytest -s

# Windows with PowerShell
$env:DEBUG="pw:api"
pytest -s
```



# 命令行工具

## 用法

```shell
% playwright
Usage: npx playwright [options] [command]

Options:
  -V, --version                          显示版本号
  																			
  -h, --help                             显示帮助文档
  																			 

Commands:
  1 打开浏览器
  open [options] [url]                   打开浏览器，并可以通过 -b, --browser 指定浏览器
  示例 playwright open www.baidu.com      打开浏览器

	2 录制功能
  codegen [options] [url]                打开浏览器 并开始录制
  
  示例 playwright codegen -b webkit www.baidu.com   打开百度，启动录制，之后点击页面元素即可录制文件
  
  
  3 debug
  debug <app> [args...]                  run command in debug mode: disable timeout, open inspector
 																				 以debug模式运行，：关闭 响应超时，打开检查器
  4 安装浏览器
  install [options] [browser...]         保证必要浏览器已安装
  
  install-deps [browser...]              安装运行浏览器所需的依赖项(将要求sudo许可)
  cr [options] [url]                     open page in Chromium
  ff [options] [url]                     open page in Firefox
  wk [options] [url]                     open page in WebKit
  screenshot [options] <url> <filename>  抓取页面截屏
  pdf [options] <url> <filename>         将页面保存为pdf
  show-trace [options] [trace]           显示追踪查看器
  help [command]                         查查看帮助

```





## <span id='installBrowsers'>install browsers</span>

运行以下命令，将会安装默认浏览器（包含Chromium、Firefox和WebKit三种），这将会花费一些时间。

```shell
playwright install
```

也可以显式指定要安装的浏览器类型：

```shell
playwright install webkit
```

查看所有支持的浏览器类型：

```shell
playwright install --help
...
Install custom browsers, supports chromium, chrome, chrome-beta, msedge, msedge-beta, msedge-dev, firefox, webkit
```

>   补充： 在某些Linux发行版上，还需要安装浏览器依赖，详情可参考`playwright install-deps --help`

## codegen

```shell
playwright codegen sspai.com
示例 playwright codegen -b webkit www.baidu.com   打开百度，启动录制，之后点击页面元素即可录制文件
  
  Options:
  -o, --output <file name>     将生成的脚本保存成文件
  --target <language>          指定语言，默认python，语言有：javascript, test, python, python-async, csharp
  -b, --browser <browserType>  指定浏览器, 浏览器有：cr, chromium, ff, firefox, wk, webkit (默认:Chrome	）															
  --channel <channel>          指定chromum供给渠道, "chrome", "chrome-beta", "msedge-dev", 等
  --color-scheme <scheme>      选择模拟颜色方案, "light" or "dark"
  --device <deviceName>        模拟设备, 	举例  "iPhone 11"  
  														 举例：playwright codegen www.baidu.com  --device "iPhone 11"

  --geolocation <coordinates>  指定地理坐标, for example "37.819722,-122.478611"
  --ignore-https-errors        跳过 https 错误
  --load-storage <filename>    从文件加载上下文存储状态 （之前使用save- storage保存的文件）  --save-storage
  --lang <language>            specify language / locale, for example "en-GB"
  --proxy-server <proxy>       specify proxy server, for example "http://myproxy:3128" or 																								 "socks5://myproxy:8080"
  --save-storage <filename>    保存文件状态, 为了之后使用 --load-storage
  --timezone <time zone>       模拟时区 for example "Europe/Rome"
  --timeout <timeout>          timeout for Playwright actions in milliseconds (default: "10000")
  --user-agent <ua string>     specify user agent string
  --viewport-size <size>       specify browser viewport size in pixels, for example "1280, 720"

	录制 的问题 ：
	1 无法录制的操作：hover，等待，上下滑
```

运行codegen并在浏览器中执行操作，Playwright CLI将根据用户交互自动生成指定语言的代码，并且codegen生成的代码中将优先使用弹性的页面元素选择器。

>     补充：什么是弹性的页面元素选择器？
>
>   Playwright可以依靠面向用户的字符串，如文本内容和label标签来选择元素，这些字符串往往比紧密耦合到DOM结构的选择器更有弹性。

![](https://tva1.sinaimg.cn/large/008i3skNgy1gu6ydkhosxj617p0f077r02.jpg)



>   补充：经过实际测试，macOS下，如果在环境变量中设置了`PWDEBUG=console pytest -s`，是无法通过codegen录制生成代码的。



### 保持身份验证状态

运行以下命令，将 cookies 和 localStorage保存在本地的`auth.json` 文件中，这有助于单独记录身份验证步骤并在以后重用。

```shell
playwright codegen --save-storage=auth.json sspai.com


playwright codegen --save-storage=auth.json https://vms-t2.tezign.com/user/login

#  补充：默认生成的 cookies 保存在 项目目录下 ，不需要指定路径，只需要填写 文件名称（auth.jasomn）
```

使用`--load storag`加载之前的存储数据，所有Cookie和localStorage都将恢复，大多数web应用程序将会处于用户身份已验证状态。

```shell
playwright open --load-storage=auth.json sspai.com
playwright codegen --load-storage=auth.json sspai.com

# 补充 playwright codegen --load-storage=auth.json https://vms-t2.tezign.com/ai/lab
# 读取刚才的保存的文件，可以直接进入对应页面，不需要再登录验证

```



### ？？自定义设置的codegen

如果想在某些非标准设置中使用codegen，例如`browser_context.route(url，handler))`，可以调用`page.pause()`，它将打开一个包含codegen控件的单独窗：

```python
# sync
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Make sure to run headed.
    browser = p.chromium.launch(headless=False)

    # Setup context however you like.
    context = browser.new_context() # Pass any options
    context.route('**/*', lambda route: route.continue_())

    # Pause the page, and start recording manually.
    page = context.new_page()
    page.pause()
    
# async
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Make sure to run headed.
        browser = await p.chromium.launch(headless=False)

        # Setup context however you like.
        context = await browser.new_context() # Pass any options
        await context.route('**/*', lambda route: route.continue_())

        # Pause the page, and start recording manually.
        page = await context.new_page()
        await page.pause()

asyncio.run(main())
```



## Open pages

通过open命令，您可以使用Playwright绑定的浏览器浏览网页。查看命令帮助：

```shell
Usage: npx playwright open [options] [url]

open page in browser specified via -b, --browser

Options:
  -b, --browser <browserType>  browser to use, one of cr, chromium, ff, firefox, wk, webkit (default: "chromium")
  --channel <channel>          Chromium distribution channel, "chrome", "chrome-beta", "msedge-dev", etc
  --color-scheme <scheme>      emulate preferred color scheme, "light" or "dark"
  --device <deviceName>        emulate device, for example  "iPhone 11"
  --geolocation <coordinates>  specify geolocation coordinates, for example "37.819722,-122.478611"
  --ignore-https-errors        ignore https errors
  --load-storage <filename>    load context storage state from the file, previously saved with --save-storage
  --lang <language>            specify language / locale, for example "en-GB"
  --proxy-server <proxy>       specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"
  --save-storage <filename>    save context storage state at the end, for later use with --load-storage
  --timezone <time zone>       time zone to emulate, for example "Europe/Rome"
  --timeout <timeout>          timeout for Playwright actions in milliseconds (default: "10000")
  --user-agent <ua string>     specify user agent string
  --viewport-size <size>       specify browser viewport size in pixels, for example "1280, 720"
  -h, --help                   display help for command

Examples:

  $ open
  $ open -b webkit https://example.com
```

示例：

```shell
# Open page in Chromium
playwright open sspai.com

# Open page in WebKit
playwright open -b wk sspai.com
```

### 设备仿生

open命令可以模拟playwright.devices列表中的移动和平板电脑设备打开浏览器。

```shell
playwright open --device="iPhone 11" example.com
```

>   补充： 要查看所有playwright支持的仿生设备，可通过以下方法：
>
>   ```python
>   from playwright.sync_api import sync_playwright
>   
>   
>   def run(playwright):
>       print(playwright.devices)		# 105个
>   
>   
>   with sync_playwright() as playwright:
>       run(playwright)
>   ```



### 模拟颜色方案和窗口大小

```shell
playwright open --viewport-size=800,600 --color-scheme=dark example.com
```



### ？？模拟地理位置、语言和时区

```shell
playwright open --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com
```



## ？？Inspect selectors

在使用 open 或 codegen 命令期间，您可以在任何浏览器的developer tools控制台中使用以下API：

-   playwright.$(selector)

    根据selector，查询匹配的页面元素；

-   playwright.$$(selector)

    和 playwright.$(selector) 类似，但是会返回所有匹配的元素（数组形式）；

    ![](https://tva1.sinaimg.cn/large/008i3skNgy1gu6zydl7c0j60ql09z40602.jpg)

-   playwright.inspect(selector)

    在 Elements 面板显示此元素（如果相应浏览器的DevTools支持它）；

-   playwright.selector(element)

    为给定元素生成选择器。

    

>   补充：打开WebKit Web Inspector将断开playwright与浏览器的连接。在这种情况下，codegen功能将无法工作。





## screenshot

查看命令帮助：

```shell
pw screenshot -h
Usage: npx playwright screenshot [options] <url> <filename>

capture a page screenshot

Options:
  --wait-for-selector <selector>  wait for selector before taking a screenshot
  --wait-for-timeout <timeout>    wait for timeout in milliseconds before taking a screenshot
  --full-page                     whether to take a full page screenshot (entire scrollable area)
  -b, --browser <browserType>     browser to use, one of cr, chromium, ff, firefox, wk, webkit (default: "chromium")
  --channel <channel>             Chromium distribution channel, "chrome", "chrome-beta", "msedge-dev", etc
  --color-scheme <scheme>         emulate preferred color scheme, "light" or "dark"
  --device <deviceName>           emulate device, for example  "iPhone 11"
  --geolocation <coordinates>     specify geolocation coordinates, for example "37.819722,-122.478611"
  --ignore-https-errors           ignore https errors
  --load-storage <filename>       load context storage state from the file, previously saved with --save-storage
  --lang <language>               specify language / locale, for example "en-GB"
  --proxy-server <proxy>          specify proxy server, for example "http://myproxy:3128" or "socks5://myproxy:8080"
  --save-storage <filename>       save context storage state at the end, for later use with --load-storage
  --timezone <time zone>          time zone to emulate, for example "Europe/Rome"
  --timeout <timeout>             timeout for Playwright actions in milliseconds (default: "10000")
  --user-agent <ua string>        specify user agent string
  --viewport-size <size>          specify browser viewport size in pixels, for example "1280, 720"
  -h, --help                      display help for command

Examples:

  $ screenshot -b webkit https://example.com example.png
```

示例：

```shell
# Wait 3 seconds before capturing a screenshot after page loads ('load' event fires)
playwright screenshot \
    --device="iPhone 11" \
    --color-scheme=dark \
    --wait-for-timeout=3000 \
    sspai.com sspai-iphone11.png
```

 ![](https://tva1.sinaimg.cn/large/008i3skNgy1gu707uwiv0j60ac0h0jsa02.jpg)



```shell
# 自动滑动页面进行截图(截全页面)
playwright screenshot --full-page sspai.com sspai-full.png


# 示例 
playwright screenshot \
     --color-scheme=dark \
	   --wait-for-timeout=3000 \
	   --full-page \
	     www.baidu.com \
	     twitter-iphone.png

```



## Generate PDF

此命令仅在无头模式下运行Chromium浏览器时支持。

```shell
playwright pdf sspai.com sspai.pdf
```



## 安装系统依赖

Ubuntu 18.04和Ubuntu 20.04系统依赖项可以自动安装。这对于CI环境来说非常有用。

```shell
playwright install-deps
playwright install-deps chromium
```



# 支持的语言

Playwright有多种语言实现的API版本。

## JavaScript and TypeScript[#](https://playwright.dev/python/docs/languages#javascript-and-typescript)

[Playwright for Node.js](https://playwright.dev/docs/intro/) is available.

-   [NPM](https://www.npmjs.com/package/playwright)
-   [Documentation](https://playwright.dev/docs/intro/)
-   [API](https://playwright.dev/docs/api/class-playwright)
-   [GitHub repo](https://github.com/microsoft/playwright)



## Python[#](https://playwright.dev/python/docs/languages#python)

[Playwright for Python](https://playwright.dev/python/docs/intro/) is available.

-   [Documentation](https://playwright.dev/python/docs/intro/)
-   [API](https://playwright.dev/python/docs/api/class-playwright)
-   [Playwright on PyPI](https://pypi.org/project/playwright/)
-   [GitHub repo](https://github.com/microsoft/playwright-python)
-   [Pytest integration](https://github.com/microsoft/playwright-pytest)



## Java[#](https://playwright.dev/python/docs/languages#java)

[Playwright for Java](https://playwright.dev/java/docs/intro/) is available.

-   [Documentation](https://playwright.dev/java/docs/intro/)
-   [API](https://playwright.dev/java/docs/api/class-playwright)
-   [GitHub repo](https://github.com/microsoft/playwright-java)





## .NET[#](https://playwright.dev/python/docs/languages#net)

[Playwright for .NET](https://playwright.dev/dotnet/docs/intro/) is available.

-   [Documentation](https://playwright.dev/dotnet/docs/intro/)
-   [API](https://playwright.dev/dotnet/docs/api/class-playwright)
-   [GitHub repo](https://github.com/microsoft/playwright-dotnet)
-   [Playwright on NuGet](https://www.nuget.org/packages/Microsoft.Playwright)



# 版本说明

[Playwright Release](https://playwright.dev/python/docs/release-notes)



# pytest 插件

使用[Pytest](https://docs.pytest.org/en/stable/)为您的 Web 应用程序编写端到端测试。

​	·用法

​	·CL I参数

​	·Fixtures

​	·样例

​	·调试

​	·持续集成

## 用法

###   安装

```shell
pip install pytest-playwright
```

使用 `page` fixture 编写基本测试 

```python
# test_my_application.py
def test_example_is_working(page):
    page.goto("https://example.com")
    assert page.inner_text('h1') == 'Example Domain'
    page.click("text=More information")
```

要运行测试，请使用 pytest CLI。

```bash
# 运行测试 （默认使用 chrome 无头模式）
pytest

# 运行测试 （有浏览器模式）
pytest --headed

# 使用不同的浏览器运行测试 (chromium, firefox, webkit)
pytest --browser firefox

# 多浏览器运行测试
pytest --browser chromium --browser webkit
```

如果要自动添加 CLI 参数而不指定它们，可以使用[pytest.ini](https://docs.pytest.org/en/stable/reference.html#ini-options-ref)文件

## CLI 参数[#](https://playwright.dev/python/docs/1.14/test-runners#cli-arguments)

- `--headed`：在有头模式下运行测试（默认：无头）。
- `--browser`：运行测试在不同的浏览器`chromium`，`firefox`或`webkit`。可以多次指定（默认：所有浏览器）。
- `--browser-channel` 要使用的[浏览器频道](https://playwright.dev/python/docs/1.14/browsers)。
- `--slowmo` 用慢动作运行测试。
- `--device` 要模拟的[设备](https://playwright.dev/python/docs/1.14/emulation)。
- `--output`测试生成的工件的目录（默认值：）`test-results`。
- `--tracing`是否记录每个测试的[轨迹](https://playwright.dev/python/docs/1.14/trace-viewer)。`on`、`off`、 或`retain-on-failure`（默认：`off`）。
- `--video`是否为每次测试录制视频。`on`、`off`、 或`retain-on-failure`（默认：`off`）。
- `--screenshot`每次测试后是否自动截屏。`on`、`off`、 或`only-on-failure`（默认：`off`）。

## Fixtures

这个插件 是playwright 特制的，fixtures，为了使用fixtures ，使用fixture名称作为测试函数的参数

```python
def test_my_app_is_working(fixture_name):
    # Test using fixture_name
    # ...
```

- **函数作用域**：这些装置在测试函数中请求时创建，并在测试结束时销毁。

  - `context`：用于测试的新[浏览器上下文](https://playwright.dev/python/docs/core-concepts#browser-contexts)。
  - `page`：用于测试的新[浏览器页面](https://playwright.dev/python/docs/core-concepts#pages-and-frames)。

  **会话范围**：这些装置在测试函数中请求时创建，并在所有测试结束时销毁。

  - `browser`：由 Playwright 启动的浏览器实例。
  - `browser_name`: 浏览器名称作为字符串。
  - `browser_channel`: 浏览器频道作为字符串。
  - `is_chromium`, `is_webkit`, `is_firefox`: 对应浏览器类型的布尔值。

  **自定义装置选项**：对于`browser`和`context`装置，使用以下装置来定义自定义启动选项。

  - `browser_type_launch_args`：覆盖[browser_type.launch(**kwargs) 的](https://playwright.dev/python/docs/1.14/api/class-browsertype#browser-type-launch)启动参数。它应该返回一个字典。
  - `browser_context_args`：覆盖[browser.new_context(**kwargs)](https://playwright.dev/python/docs/1.14/api/class-browser#browser-new-context)的选项。它应该返回一个字典。

## 示例

### 自动配置成Mypy类型

```python
# test_my_application.py
from playwright.sync_api import Page

def test_visit_admin_dashboard(page: Page):
    page.goto("/admin")
```

### 配置慢动作

使用带有`--slowmo`参数的慢速模式运行测试。

```bash
pytest --slowmo 100
```

### 通过浏览器跳过测试[#](https://playwright.dev/python/docs/test-runners#skip-test-by-browser)

```python
# test_my_application.py
import pytest

@pytest.mark.skip_browser("firefox")
def test_visit_example(page):
    page.goto("https://example.com")
    # ...
```

### 在特定浏览器上运行[#](https://playwright.dev/python/docs/test-runners#run-on-a-specific-browser)

```python
# conftest.py
import pytest

@pytest.mark.only_browser("chromium")
def test_visit_example(page):
    page.goto("https://example.com")
    
```

### 使用自定义浏览器频道运行，如 Google Chrome 或 Microsoft Edge

```bash
pytest --browser-channel chrome
```

```python
# test_my_application.py
def test_example(page):
    page.goto("https://example.com")
```



### 配置 base-url 

用`base-url`参数启动 Pytest 。

```bash
pytest --base-url http://localhost:8080
```

```python
# test_my_application.py
def test_visit_example(page):
    page.goto("/admin")
    # -> Will result in http://localhost:8080/admin
```

### 忽略 HTTPS 错误

```python
# conftest.py
import pytest

@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True
    }
```



### 使用自定义窗口大小

```python
# conftest.py
import pytest

@pytest.fixture()
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1920,
            "height": 1080,
        }
    }
```

### 设备仿真

```python
# conftest.py
import pytest

@pytest.fixture()
def browser_context_args(browser_context_args, playwright):
    iphone_11 = playwright.devices['iPhone 11 Pro']
    return {
        **browser_context_args,
        **iphone_11,
    }

```

或通过 CLI `--device="iPhone 11 Pro"`

### 环境持久化

```python
# conftest.py
import pytest
from playwright.sync_api import BrowserType
from typing import Dict

@pytest.fixture(scope="session")
def context(
    browser_type: BrowserType,
    browser_type_launch_args: Dict,
    browser_context_args: Dict
):
    context = browser_type.launch_persistent_context("./foobar", **{
        **browser_type_launch_args,
        **browser_context_args,
        "locale": "de-DE",
    })
    yield context
    context.close()
```

使用它时，测试中的所有页面都是从持续环境中创建的。

### 与unittest.TestCase一起使用

请参阅以下示例以将其与`unittest.TestCase`. 这有一个限制，即只能指定一个浏览器，并且在指定多个浏览器时不会生成多个浏览器的矩阵。

```python
import pytest
import unittest

from playwright.sync_api import Page


class MyTest(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.page = page

    def test_foobar(self):
        self.page.goto("https://microsoft.com")
        self.page.click("#foobar")
        assert self.page.evaluate("1 + 1") == 2
```

## 调试[#](https://playwright.dev/python/docs/1.14/test-runners#debugging)

### 与 pdb 一起使用

使用`breakpoint()`测试代码中的语句暂停执行并获取[pdb](https://docs.python.org/3/library/pdb.html) REPL。

```python
def test_bing_is_working(page):
    page.goto("https://bing.com")
    breakpoint()
    # ...
```

复制

## 部署到 CI [#](https://playwright.dev/python/docs/1.14/test-runners#deploy-to-ci)

请参阅[CI 提供者指南](https://playwright.dev/python/docs/1.14/ci)以将您的测试部署到 CI/CD。



 # 二 指南

## 自动等待

Playwright 在采取行动之前对元素执行一系列可操作性检查，以确保这些行动按预期运行. 它会自动等待所有相关检查通过，然后才执行请求的操作。如果所需的检查未在给定的范围内通过`timeout`，则操作将失败并显示`TimeoutError`。

- 例如，对于[page.click(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-click)，Playwright 将确保：
  - 元素被附加到 DOM
  - 元素是可见的
  - 元素是稳定的，没有在渲染中或未完成渲染
  - 元素可接受操作，因为没有被其他元素占用
  - 元素已启用

以下是为每个操作执行的可操作性检查的完整列表

| 操作                   | 附加的 | 可见的 | 稳定的 | 启用的 |      | 可编辑 |
| ---------------------- | ------ | ------ | ------ | ------ | ---- | ------ |
| check                  | Yes    | Yes    | Yes    | Yes    | Yes  | -      |
| click                  | Yes    | Yes    | Yes    | Yes    | Yes  | -      |
| dblclick               | Yes    | Yes    | Yes    | Yes    | Yes  | -      |
| tap                    | Yes    | Yes    | Yes    | Yes    | Yes  | -      |
| uncheck                | Yes    | Yes    | Yes    | Yes    | Yes  | -      |
| hover                  | Yes    | Yes    | Yes    | Yes    | -    | -      |
| scrollIntoViewIfNeeded | Yes    | Yes    | Yes    | -      | -    | -      |
| screenshot             | Yes    | Yes    | Yes    | -      | -    | -      |
| fill                   | Yes    | Yes    | -      | -      | Yes  | Yes    |
| selectText             | Yes    | Yes    | -      | -      | -    | -      |
| dispatchEvent          | Yes    | -      | -      | -      | -    | -      |
| focus                  | Yes    | -      | -      | -      | -    | -      |
| getAttribute           | Yes    | -      | -      | -      | -    | -      |
| innerText              | Yes    | -      | -      | -      | -    | -      |
| innerHTML              | Yes    | -      | -      | -      | -    | -      |
| press                  | Yes    | -      | -      | -      | -    | -      |
| setInputFiles          | Yes    | -      | -      | -      | -    | -      |
| selectOption           | Yes    | -      | -      | -      | -    | -      |
| textContent            | Yes    | -      | -      | -      | -    | -      |
| type                   | Yes    | -      | -      | -      | -    | -      |



### 强制执行

一些操作，如page.click(selector, **kwargs)支持force禁用非必要的可操作性检查的选项，例如将 truthy 传递force给page.click(selector, **kwargs)方法不会检查目标元素是否实际接收点击事件

### 断言

您也可以使用以下方法之一检查元素的可操作性状态。这通常不是必需的，但它有助于编写断言测试，确保在某些操作之后，元素达到可操作状态：

- [element_handle.is_checked()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-checked)
- [element_handle.is_disabled()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-disabled)
- [element_handle.is_editable()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-editable)
- [element_handle.is_enabled()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-enabled)
- [element_handle.is_hidden()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-hidden)
- [element_handle.is_visible()](https://playwright.dev/python/docs/1.14/api/class-elementhandle#element-handle-is-visible)
- [page.is_checked(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-checked)
- [page.is_disabled(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-disabled)
- [page.is_editable(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-editable)
- [page.is_enabled(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-enabled)
- [page.is_hidden(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-hidden)
- [page.is_visible(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-is-visible)



### 附加

当元素[连接](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected)到 Document 或 ShadowRoot时，它被认为是附加的。

### 可见

当元素具有非空边界框并且没有`visibility:hidden`计算样式时，元素被认为是可见的。请注意，零大小或 with 的元素`display:none`不被视为可见。

### 稳定

当元素在至少两个连续动画帧中保持相同的边界框时，它被认为是稳定的。

### 启用

元素被认为启用时它不是一个`<button>`，`<select>`，`<input>`或`<textarea>`具有`disabled`属性集。

### 可编辑

元素在[启用](https://playwright.dev/python/docs/1.14/actionability#enabled)且未`readonly`设置属性时被视为可编辑。

### 接收事件

当元素在动作点是指针事件的命中目标时，元素被视为接收指针事件。例如，当点击点 时`(10;10)`，Playwright 会检查其他元素（通常是叠加层）是否会在 处捕获点击`(10;10)`。

例如，考虑一个场景，`Sign Up`无论何时进行[page.click(selector, **kwargs)](https://playwright.dev/python/docs/1.14/api/class-page#page-click)调用，Playwright 都会单击按钮：

- 页面正在检查用户名是否唯一并且`Sign Up`按钮被禁用；
- 在与服务器核对后，禁用的`Sign Up`按钮被替换为另一个现在启用的按钮。

## 断言

Playwright 为常见任务提供了便利的 API，例如阅读元素的文本内容。这些 API 可用于您的测试断言。

- [文字内容](https://playwright.dev/python/docs/1.14/assertions#text-content)
- [内文](https://playwright.dev/python/docs/1.14/assertions#inner-text)
- [属性值](https://playwright.dev/python/docs/1.14/assertions#attribute-value)
- [复选框状态](https://playwright.dev/python/docs/1.14/assertions#checkbox-state)
- [JS表达式](https://playwright.dev/python/docs/1.14/assertions#js-expression)
- [内部 HTML](https://playwright.dev/python/docs/1.14/assertions#inner-html)
- [能见度](https://playwright.dev/python/docs/1.14/assertions#visibility)
- [启用状态](https://playwright.dev/python/docs/1.14/assertions#enabled-state)
- [自定义断言](https://playwright.dev/python/docs/1.14/assertions#custom-assertions)



### 断言-文字内容 

```python
# 同步
content = page.text_content("nav:first-child")
assert content == "home"

# 异步
content = await page.text_content("nav:first-child")
assert content == "home"
```

### 断言-内部文字

```python
text = page.inner_text(".selected")
assert text == "value"
```

# 五 api

## playwright

###   

返回： 无

终止此 Playwright 实例，以防它绕过 Python 上下文管理器创建。这在 REPL 应用程序中很有用。

```bash
>>> from playwright.sync_api import sync_playwright
>>> playwright = sync_playwright().start()
>>> browser = playwright.chromium.launch()
>>> page = browser.new_page()
>>> page.goto("http://whatsmyuseragent.org/")
>>> page.screenshot(path="example.png")
>>> browser.close()
>>> playwright.stop()
```

​	输入：< [BrowserType](https://playwright.dev/python/docs/1.14/api/class-browsertype) >

  此对象可用于启动或连接到 Chromium，返回[Browser 的](https://playwright.dev/python/docs/1.14/api/class-browser)实例。

### playwright.firefox 

- 输入：< [BrowserType](https://playwright.dev/python/docs/1.14/api/class-browsertype) >

此对象可用于启动或连接到 Firefox，返回[Browser 的](https://playwright.dev/python/docs/1.14/api/class-browser)实例。

### playwright.devices 

- 类型：<[字典]>

返回要与[browser.new_context(**kwargs)](https://playwright.dev/python/docs/1.14/api/class-browser#browser-new-context)或[browser.new_page(**kwargs)](https://playwright.dev/python/docs/1.14/api/class-browser#browser-new-page)一起使用的设备字典。

- ```python
  # 同步
  from playwright.sync_api import sync_playwright
  
  def run(playwright):
      webkit = playwright.webkit
      # 选取设备
      iphone = playwright.devices["iPhone 6"]
      browser = webkit.launch()
      # 通过new_context 	启动新的浏览器context 它不会与其他浏览器context共享cookie/缓存
      context = browser.new_context(**iphone)
      page = context.new_page()
      page.goto("http://example.com")
      # other actions...
      browser.close()
  
  with sync_playwright() as playwright:
      run(playwright)
      
  # 异步实现
  import asyncio
  from playwright.async_api import async_playwright
  
  async def run(playwright):
      webkit = playwright.webkit
      iphone = playwright.devices["iPhone 6"]
      browser = await webkit.launch()
      context = await browser.new_context(**iphone)
      page = await context.new_page()
      await page.goto("http://example.com")
      # other actions...
      await browser.close()
  
  async def main():
      async with async_playwright() as playwright:
          await run(playwright)
  asyncio.run(main())
  ```
  
  
  ## Classes
  
  ### 持久上下文[#](https://playwright.dev/python/docs/test-runners#persistent-context)
  
  ```
  
  [pytest]
  # 命令行参数，用空格分隔
  addopts = -vs
  
  # 测试用例文件夹，可配置
  testpaths = ../watchmen/case
  
  #配置测试搜索的模块文件名称
  python_files = test_*.py
  
  #配置测试搜索的测试类名
  python_classes=Test*
  
  #配置测试搜索的测试函数名
  python_functions = test
  
  #分组内容
  markers =
      p0: 主流程功能用例
      p1：备选测试流程
      p2：异常测试流程
      smoke：冒烟用例
      user：用户管理模块
  
  
  
  ```
  
  
  
  
  
  



