from fastmcp import FastMCP
from datetime import datetime
import random
import math
from fastmcp import FastMCP
import requests

# 创建MCP服务实例
mcp = FastMCP(name='RISK-LLM')

# 注册工具：打招呼
@mcp.tool
def greet(name: str) -> str:
    """打招呼"""
    return f"Hello, {name}!"

# 注册工具：获取当前时间
@mcp.tool
def get_current_time() -> str:
    """返回当前时间"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 注册工具：生成随机数
@mcp.tool
def generate_random_number(min: int = 0, max: int = 100):
    """生成指定范围内的随机数"""
    return random.randint(min, max)

# 注册工具：计算平方根
@mcp.tool
def calculate_square_root(number: float) -> float:
    """计算给定数字的平方根"""
    if number < 0:
        raise ValueError("无法计算负数的平方根")
    return math.sqrt(number)

# 注册工具：获取最新判决文书
@mcp.tool
def get_latest_judgment(credit_code: str) -> str:
    """返回最新的判决文书内容"""
    # 这里可以根据credit_code查询最新的判决文书内容
    if not credit_code:
        raise ValueError("信用代码不能为空")
    
    return "一、被告上海某某贸易有限公司于本判决生效之日起十日内支付原告货款100000元及利息"

# 注册工具：获取客户风险信
@mcp.tool
def get_risk_info(credit_code: str) -> str:
    """测试获取客户风险信息"""
    # 这里可以根据credit_code查询最新的判决文书内容
    if not credit_code:
        raise ValueError("信用代码不能为空")

    # API基础URL
    BASE_URL = "http://localhost:8012"
    """测试获取客户风险信息"""
    url = f"{BASE_URL}/risk-info/{credit_code}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return str(response.json())
        else:
            return f"查询失败，状态码: {response.status_code}"
    except Exception as e:
        return f"查询出错: {e}"


if __name__ == "__main__":
    # 启动服务
    mcp.run(
        transport="streamable-http",
        host="0.0.0.0", 
        port=8011,
        path="/mcp"
    )