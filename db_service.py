import sqlite3
import json

# 连接到SQLite数据库
def get_db_connection():
    conn = sqlite3.connect('/Users/jiahaoluo/Desktop/SHOW-ME-THE-CODE/risk-llm-mcp/risk_data.db')
    conn.row_factory = sqlite3.Row
    return conn

# 初始化数据库和表
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 创建客户风险信息表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_risk_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        credit_code TEXT UNIQUE NOT NULL,
        company_name TEXT NOT NULL,
        registration_date TEXT,
        registered_capital TEXT,
        employee_count INTEGER,
        risk_level TEXT NOT NULL,
        judgment_content TEXT,
        latest_update_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 插入一些示例数据
    cursor.execute('''
    INSERT OR IGNORE INTO customer_risk_info (credit_code, company_name, registration_date, registered_capital, employee_count, risk_level, judgment_content)
    VALUES
        ('91330105MADWLBFF2J', '伊犁某某科技有限公司', '2020-05-15', '100万元', 25, '高风险', '一、2024年7月18日原告伊犁某某科技有限公司与被告R某某签订的《股权转让协议》于2024年10月24日解除；二、被告R某某于本判决生效之日起十日内支付原告伊犁某某科技有限公司违约金55000元；三、被告R某某于本判决生效之日起十日内支付原告伊犁某某科技有限公司律师代理费10000元；四、驳回原告伊犁某某科技有限公司的其他诉讼请求。如果未按本判决指定的期间履行给付金钱义务，应当依照《中华人民共和国民事诉讼法》第二百六十四条规定，加倍支付迟延履行期间的债务利息。案件受理费12229.14元，减半收取6114.57元（原告已预交），由原告伊犁某某科技有限公司负担5643.05元，由被告R某某负担471.52元。如不服本判决，可以在判决书送达之日起十五日内，向本院递交上诉状，并按照对方当事人或者代表人的人数提出副本，上诉于新疆维吾尔自治区高级人民法院伊犁哈萨克自治州分院；也可以在判决书送达之日起十五日内，向新疆维吾尔自治区高级人民法院伊犁哈萨克自治州分院在线提交上诉状'),
        ('91330105MADWLBFF2K', '杭州某某信息技术有限公司', '2018-12-03', '500万元', 120, '低风险', '无重大判决记录'),
        ('91330105MADWLBFF2K', '杭州某某信息技术有限公司', '2018-12-03', '500万元', 200, '高风险', '无重大判决记录'),
        ('91330105MADWLBFF2L', '上海某某贸易有限公司', '2021-03-22', '200万元', 45, '中风险', '一、被告上海某某贸易有限公司于本判决生效之日起十日内支付原告货款100000元及利息')
    ''')
    
    conn.commit()
    conn.close()

# 根据信用代码查询客户风险信息
def get_customer_risk_info(credit_code):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM customer_risk_info WHERE credit_code = ?
    ''', (credit_code,))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return dict(result)
    else:
        return None

# 数据服务
class RiskInfoDBService:
    def __init__(self):
        init_db()
    
    def get_risk_info(self, credit_code):
        """根据信用代码获取客户风险信息"""
        risk_info = get_customer_risk_info(credit_code)
        if risk_info:
            return risk_info
        else:
            return "未查询到客户风险信息"