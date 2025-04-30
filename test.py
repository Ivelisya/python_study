from github import Github

# 替换为你的 Personal Access Token
ACCESS_TOKEN = "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"

# 替换为你的 GitHub 用户名
USERNAME = "ivelisya"

# 初始化 GitHub 客户端
g = Github(ACCESS_TOKEN)
user = g.get_user(USERNAME)

# 获取所有仓库
repos = user.get_repos()

# 遍历所有仓库，并将它们设置为公有
for repo in repos:
    try:
        if repo.private:  # 检查是否已经是私有仓库
            repo.edit(private=False)
            print(f"仓库 {repo.name} 已设置为公有")
        else:
            print(f"仓库 {repo.name} 已经是公有仓库")
    except Exception as e:
        print(f"设置仓库 {repo.name} 为公有时出错: {e}")

print("完成！")
