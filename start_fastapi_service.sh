#!/bin/bash

# 启动MCP服务
echo "启动MCP服务..."
python /Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm-mcp/server.py &
SERVER_PID=$!

echo "等待MCP服务启动..."
sleep 3

# 启动FastAPI服务
python /Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm-mcp/fastapi_service.py &
FASTAPI_PID=$!

echo "等待API服务启动..."
sleep 3

# 启动FastAPI-MCP服务
python /Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm-mcp/fastapi_mcp_service.py &
FASTAPI_PID=$!

echo "等待API服务启动..."
sleep 3

# 运行测试
echo "运行测试..."
python /Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm-mcp/client.py

# 停止服务
echo "停止MCP服务..."
kill $SERVER_PID

# 停止服务
echo "停止API服务..."
kill $FASTAPI_PID

echo "测试完成!"