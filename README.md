# Flask TodoList 应用

一个使用 Flask 开发的简单 TodoList 任务管理应用，支持任务的增删改查和数据持久化存储。

## 特性

- 简单易用 - 直观的用户界面，轻松管理日常任务
- 数据持久化 - 任务数据保存在 JSON 文件中，无需数据库
- 响应式设计 - 支持桌面和移动设备
- 实时更新 - 通过 AJAX 实现页面无刷新操作
- 统计信息 - 实时显示任务完成情况统计
- RESTful API - 完整的 API 接口，便于扩展

## 技术栈

- 后端: Flask 3.1.2
- 前端: HTML5, CSS3, JavaScript (原生)
- 数据存储: JSON 文件
- 包管理: UV
- 运行环境: Python 3.12+

## 安装和运行

### 环境要求

- Python 3.12+
- UV (Python 包管理工具)

### 安装步骤

1. 克隆或下载项目
   ```bash
   git clone <repository-url>
   cd flask-todolist
   ```

2. 安装依赖
   ```bash
   uv install
   ```

3. 启动应用
   ```bash
   uv run python app.py
   ```

4. 访问应用
   在浏览器中打开：http://127.0.0.1:5000

## 使用说明

### 基本操作

1. 添加任务
   - 在输入框中输入任务标题
   - 点击"添加任务"按钮或按回车键

2. 标记完成/未完成
   - 点击任务前的复选框切换状态
   - 已完成的任务会有特殊样式显示

3. 删除任务
   - 点击任务右侧的"删除"按钮
   - 确认后任务将被永久删除

4. 查看统计
   - 页面底部显示任务总数、已完成数和待完成数

### 数据存储

- 所有任务数据保存在 todos.json 文件中
- 文件采用 UTF-8 编码，支持中文
- 数据格式为 JSON，便于备份和迁移

## API 接口

### 获取所有任务
```
GET /api/todos
```

响应示例：
```json
[
  {
    "id": 1,
    "title": "学习 Flask",
    "description": "完成 Flask 教程",
    "completed": false,
    "created_at": "2025-11-10T02:30:00.000000",
    "completed_at": null
  }
]
```

### 添加新任务
```
POST /api/todos
Content-Type: application/json

{
  "title": "任务标题",
  "description": "任务描述（可选）"
}
```

### 更新任务
```
PUT /api/todos/{id}
Content-Type: application/json

{
  "title": "新的标题",
  "completed": true
}
```

### 删除任务
```
DELETE /api/todos/{id}
```

### 切换任务状态
```
POST /api/todos/{id}/toggle
```

## 项目结构

```
flask-todolist/
├── app.py              # Flask 主应用文件
├── todo_manager.py     # 任务数据管理类
├── templates/
│   └── index.html      # 前端页面模板
├── todos.json          # 数据存储文件（自动生成）
├── pyproject.toml      # 项目配置文件
└── README.md          # 项目说明文档
```

## 开发说明

### 核心模块

1. todo_manager.py - 任务数据管理类
   - 负责数据的读取、写入和操作
   - 提供完整的 CRUD 操作接口

2. app.py - Flask 主应用
   - 定义路由和处理函数
   - 提供 Web 页面和 API 接口

3. templates/index.html - 前端页面
   - 响应式设计，支持移动端
   - 使用原生 JavaScript 实现 AJAX 交互

### 扩展建议

- 添加用户认证和授权
- 支持任务分类和标签
- 添加任务优先级
- 实现任务搜索和过滤
- 添加任务提醒功能
- 支持导入/导出功能

## 故障排除

### 常见问题

1. 端口被占用
   ```bash
   # 修改 app.py 中的端口号
   app.run(debug=True, port=5001)
   ```

2. 数据文件权限问题
   - 确保应用有权限读写 todos.json 文件
   - 检查文件目录的写入权限

3. 依赖安装失败
   ```bash
   # 清除缓存重新安装
   uv cache clean
   uv install
   ```

## 许可证

本项目采用 MIT 许可证。

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

---

Made with love using Flask and UV