from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from db_service import RiskInfoDBService

# 创建fastapi应用
app = FastAPI(title="客户风险信息API服务", description="提供客户风险信息查询接口")

# 初始化RiskInfoDBService
risk_db_service = RiskInfoDBService()

@app.get("/risk-info/{credit_code}", tags=["风险信息查询"])
async def get_risk_info(credit_code: str):
    """
    根据信用代码获取客户风险信息
    
    参数:
        credit_code: 客户信用代码
    
    返回:
        客户风险信息或未找到的提示
    """
    return risk_db_service.get_risk_info(credit_code)

# ================================================================================================
mcp = FastApiMCP(app, name="客户风险信息查询")

# 将MCP服务器直接挂载到你的FastAPI应用上
mcp.mount()
# ================================================================================================


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8014)