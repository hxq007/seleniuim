**git 账号@hxq001  2280316018@qq.com  密码 hxqlovewmz1314**
**git 命令** 
**cat 文件名 查看文件内容** 
**cd ~ 进入主目录**
**tab   自动 补全文件** 
**clear 清屏**
**git --version git内查看git版本** 
**git config --global user.name "用户名"  设置用户名**
**git config --global user.email "邮箱"    设置邮箱**
**git init  本地仓库初始化**
**ll -la   查看隐藏文件**
**git add 文件名  将文件提交在暂存区**
**git commit -m ""  将暂存区的文件放在本地库 冒号里面是 备注**
**git status 知道git工作区和暂存的文件状态**
**日志展示方式  
1、git log  分页查看git 日志    查询日志分页分屏   到下一页 空格 上一页 b  退出q**
**2、git log --pretty=oneline  查看日志索引**
**3、git log --oneline  截取7位索引展示**
**4、git reflog     展示 head@{数字}  数字代表代表回到那个版本需要回到哪一步**
**git reset --hard 索引  版本回退至索引版本  hard参数  本地库移动的同时   重置暂存区 重置工作区**
**mixed 参数  本地库的指针移动的时候 重置暂存区 工作区不动** 
**soft 参数  本地库指针移动的时候 暂存区和工作区都不动**
**rm 文件名 删除工作区文件 然后再输入 提交暂存和本地命令 同步三个区域**
**git diff文件名 比对工作区和暂存区的 git文件内容差异  git diff 加索引 比对暂存区和本地库的差异** 
**git branch -v 查看git下的所有分支**
**git branch 分支名 创建分支** 
**git push --set-upstream origin dev //dev为创建分支的名字 origin别名  向远程仓库新增分支**
**git push origin 分支名 --force 强制提交本地分支覆盖远程分支**
**git checkout 分支名 切换分支**
**git merge 分支名  合并分支  合并冲突问题 1、内部删除留下需要的**
**git remote -v 查看远程仓库地址别名**
**git remote add 别名 远程仓库地址    ———————给远程仓库地址起别名  fetch 拉取东西 push 推送东西**
**git pull --rebase 仓库地址别名 master 获取远程库与本地同步合并（如果远程库不为空必须做这一步，否则后面的提交会失败）**
**git pull 别名 分支名 --allow-unrelated-historis  拉取毫不相关远程仓库的代码**
**git push 别名 分支名 向远程仓库推送分支** 
**git push -u 别名 分支名 -f 推送至远程分支**
**git clone 远程仓库地址   克隆远程仓库内容(1、初始化本地库2、远程库内容完整克隆本地3、创建远程库别名) 人员**
**git fetch 别名 分支名  拉取远程仓库文件下载到本地** 
**git merge 别名/分支   将远程仓库下载到本地的文件 进行合并   pull 操作等于 fetch+merge 加起来的命令  git pull 别名 分支**
**向远程仓库 推送分支 有冲突 应该先将远程库内容下载下来留下需要的 在重新推送 (人为解决)  冲突时 commit 后面不加文件名** 
**ssh-keygen -t rsa -C 2280316018@qq.com  ssh秘钥登录 邮箱为git账号  免登陆方式  生成ssh目录的命令  
ider 集成git**













