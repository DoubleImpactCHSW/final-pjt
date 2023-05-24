<template>
  <div class="detail-container">
    <div class="detail-section">
      <span class="detail-label">제목</span>
      <span class="detail-title-value">{{ title }}</span>
    </div>
    <div class="detail-section">
      <span class="detail-label">작성자</span>
      <span class="detail-value">{{ writer }}</span>
    </div>
    <div class="detail-section">
      <span class="detail-label">작성일</span>
      <span class="detail-value">{{ newCreatedAt }}</span>
    </div>
    <div class="detail-section detail-content">
      <span class="detail-label">내용</span>
      <div class="content-box">
        <div class="content-scroll">
          <span class="detail-value content-text">{{ content }}</span>
        </div>
      </div>
    </div>
    <b-button @click="goEdit" v-if="inMine" variant="success">수정</b-button>
  </div>
</template>

<script>
export default {
  name: 'DetailContent',

  props: {
    writer: String,
    title: String,
    content: String,
    createdAt: String,
  },

  computed: {
    inMine() {
      return this.writer === this.$store.state.username;
    },
    newCreatedAt() {
      const date = new Date(this.createdAt);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
  
      return `${year}년 ${month}월 ${day}일`;
    }
  },

  methods: {
    goEdit() {
      this.$store.dispatch('changeCommunityMode', 'edit');
    },
  },
};
</script>

<style scoped>
.detail-container {
  max-width: 600px; /* 원하는 최대 너비로 설정 */
  margin: 0 auto; /* 가운데 정렬을 위해 margin 설정 */
  background-color: #f8f8f8;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-bottom: 20px;
}

.detail-section {
  display: flex;
  margin-bottom: 10px;
}

.detail-label {
  font-size: 16px;
  font-weight: bold;
  width: 80px;
  color: #666;
}

.detail-value {
  font-size: 16px;
}

.detail-title-value {
  font-size: 16px;
  font-weight: 600;
}

.detail-content {
  align-items: flex-start;
}

.content-box {
  background-color: #fff;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 5px;
  width: 100%;
  height: 200px; /* 고정된 높이 설정 */
  overflow: auto; /* 스크롤 가능하도록 설정 */
}

.content-scroll {
  width: 100%;
  height: max-content; /* 내용의 크기에 맞춰 높이 설정 */
}

.content-text {
  display: block;
  white-space: pre-wrap; /* 줄바꿈 처리 */
  word-break: break-all; /* 단어가 줄 바꿈되도록 처리 */
  text-align: left; /* 왼쪽 정렬 설정 */
}

.b-button {
  margin-top: 10px;
}
</style>