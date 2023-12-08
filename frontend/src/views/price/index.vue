<template>
  <div class="container">
    <h1 class="title" style="color: #1a237e">World Chat AI Pricing Plans</h1>
    
    <div class="pricing-sections">
      <div class="pricing-section">
        <h2>聊天服务</h2>
        <div class="plan">
          <div class="plan-header">标准版</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i>每月: ¥5 | 每年: ¥50</div>
        </div>
            <br>
        <div class="plan">
          <div class="plan-header">增强版</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i>每月: ¥45 | 每年: ¥450</div>
        </div>
      </div>

      <div class="pricing-section">
        <h2>代理服务</h2>
        <div class="plan">
          <div class="plan-header">标准版</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i> 每月: ¥10 | 每年: ¥100</div>
        </div>
            <br>
        <div class="plan">
          <div class="plan-header">增强版</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i> 每月: ¥30 | 每年: ¥300</div>
        </div>
      </div>

      <div class="pricing-section">
        <h2>捆绑购买</h2>
        <div class="plan">
          <div class="plan-header">标准聊天服务 + 标准代理服务</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i> 每月: ¥12 | 每年: ¥120</div>
        </div>
            <br>
        <div class="plan">
          <div class="plan-header">增强聊天服务 + 标准代理服务</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i>增强聊天服务赠送标准代理服务</div>
        </div>
        <br>
        <div class="plan">
          <div class="plan-header">增强聊天服务 + 增强代理服务</div>
          <div class="plan-price"><i class="icon fas fa-tag"></i> 每月: ¥60 | 每年: ¥600</div>
        </div>
      </div>
    </div>

    <div class="contact-info">
      <!-- Contact Information section -->
      <h3>请通过邮件联系我们进行注册: wca@fushisanlang.cn</h3>
      <h3>或者添加如下企业微信联系人: </h3>
      <img class="qr-code" src="/public/wx.png" alt="QR Code">
    </div>
  </div>
</template>


<script>
export default {
  // Add your Vue component logic here, if needed
}
</script>

<style>
/* Add your CSS styles here */
body {
  font-family: 'Arial', sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f5f5f5;
}




.note-section {
  margin-top: 30px;
  font-size: 16px;
  color: #666;
}






.h1 {
  font-size: 50px;
}
.h3 {
  font-size: 20px;
  margin-bottom: 15px;
  color: #d7ccc8; /* 修改小标题颜色 */
}
.container {
  width: 90%;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
}

.title {
  font-size: 24px;
  margin-bottom: 20px;
}

.pricing-sections {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.pricing-section {
  flex: 0 1 calc(45% - 20px); /* 调整每个 section 的宽度 */
  background-color: #fff;
  border-radius: 5px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.plan-header {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #2e7d32;
}

.plan-price {
  font-size: 16px;
  color: #64b5f6;
}

.pricing-section h2 {
  font-size: 28px;
  margin-bottom: 15px;
  color: #757575;
}

.contact-info {
  text-align: center;
  margin-top: 20px;
}

.contact-info h3 {
  font-size: 18px;
  margin-bottom: 10px;
}

.qr-code {
  max-width: 100%; /* 让二维码图像适应容器宽度 */
  height: auto;
}
</style>
