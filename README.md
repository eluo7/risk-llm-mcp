# RISK-LLM-MCP

## 项目概述
risk-llm是一个基于FastAPI和MCP服务的风险信息查询系统，实现了客户风险信息的存储、查询和API服务功能。

## 功能模块

### 1. 数据库服务模块
- **功能**：实现客户风险信息的存储与查询
- **核心文件**：<mcfile name="db_service.py" path="/Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm/db_service.py"></mcfile>
- **主要功能**：
  - SQLite数据库连接与初始化
  - 客户风险信息表创建与示例数据插入
  - 按信用代码查询客户风险信息

### 2. FastAPI服务模块
- **功能**：提供HTTP接口服务
- **核心文件**：<mcfile name="fastapi_service.py" path="/Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm/fastapi_service.py"></mcfile>
- **主要接口**：
  - `GET /risk-info/{credit_code}`：根据信用代码查询风险信息

### 3. MCP服务模块
- **功能**：提供多种工具函数的MCP服务
- **核心文件**：<mcfile name="server.py" path="/Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm/server.py"></mcfile>
- **主要工具**：
  - 基础工具：greet(打招呼)、get_current_time(获取时间)、generate_random_number(生成随机数)、calculate_square_root(计算平方根)
  - 业务工具：get_latest_judgment(获取最新判决文书)、get_risk_info(获取客户风险信息)

### 4. 客户端测试模块
- **功能**：测试MCP服务的客户端示例
- **核心文件**：<mcfile name="client.py" path="/Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm/client.py"></mcfile>
- **主要功能**：连接MCP服务并测试所有工具函数调用

## 项目结构
```
risk-llm/
├── README.md              # 项目文档
├── db_service.py          # 数据库服务模块
├── fastapi_service.py     # FastAPI服务模块
├── server.py              # MCP服务模块
├── client.py              # 客户端测试模块
├── requirements.txt       # 项目依赖
└── start_fastapi_service.sh  # 服务启动脚本
```

## 快速开始

### 1. 创建并激活虚拟环境
```bash
uv venv
source .venv/bin/activate
```

### 2. 安装依赖
```bash
uv add fastapi uvicorn fastmcp requests
```

### 3. 启动服务
```bash
# 启动MCP服务和FastAPI服务并运行测试
sh ./start_fastapi_service.sh
```
        