<template>
    <div class="left_wrap">
        <!-- 좌측 검색필터 -->

            <div class="left_wrap fixed shadow">
                <p class="tit text-start">
                    <strong class="head_txt">정기예금</strong><br>
                    <span>검색조건을 입력해주세요</span>
                </p>
  

                <form class="left_menu_inner" @submit.prevent="searchProducts">

                  <!-- 1. 예치금액 -->
                  <div class="amount_area">
                    <label class="input_label">예치금액</label>
                    <div class="input_box">
                      <input class="min amount" name="amount" maxlength="10" v-model="payload.depositAmount">
                    </div>
                  </div>

                  <!-- 2. 예치기간 -->
                  <div class="input_group all period">
                    <label class="input_label">예치기간(개월)</label>
                    <div class="input_box">
                      <select class="min select" name="term" v-model="payload.selectedTerm">
                        <option v-for="term in terms" :key="term" :value="term">{{ term }}</option>
                      </select>
                    </div>
                  </div>


                  <!-- 3. 이자율 -->
                  <div class="amount_area">
                    <label class="input_label">이자율</label>
                    <div class="input_box">
                      <input class="min interest" v-model="payload.interest" name="interest" maxlength="10">
                    </div>
                  </div>
                  
                  <!-- 4. 이자지급방식 -->
                  <div class="input_group all deposit_only" style="display: block;">
                    <label class="input_label">이자지급방식</label>
                    <div class="input_box">
                      <select class="min select" v-model="payload.selectedPaymentTerm" name="payment_term">
                        <option v-for="option in paymentTerms" :key="option" :value="option">{{ option }}</option>
                      </select>
                    </div>
                  </div>

                  <!-- 5. 지역 -->
                  <div class="input_group all">
                    <label class="input_label">지역</label>
                    <div class="input_box">
                      <select class="min select" v-model="payload.selectedRegion" name="region_sido">
                        <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
                      </select>
                    </div>
                  </div>


                  <!-- 6. 은행명 -->
                  <div class="input_gruop all">
                    <label class="input_label">은행명</label>
                    <div class="input_box">
                      <select class="min select" v-model="payload.selectBank" name="bank_sido">
                        <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
                      </select>
                    </div>
                  </div>



                  <!-- 7. 가입방식 -->
                  <div class="input_group all">
                    <label class="input_label">가입방식</label>
                    <div class="input_box">
                      <select class="min select" v-model="payload.selectedJoinChannel" name="join_channel">
                        <option v-for="channel in joinChannels" :key="channel" :value="channel">{{ channel }}</option>
                      </select>
                    </div>
                  </div>

                  <!-- 확인 / 초기화  -->
                  <div class="btn_wrap pt-4 pb-2">
                      <button type="submit" class="btn btn-primary">조회</button>
                  </div>
                  <div class="btn_wrap">
                      <button class="btn btn-secondary">초기화</button>
                  </div>

                    
                </form>
                    
  
            </div>
  

      <!-- </div> -->
    </div>
</template>

<script>
export default {
  name: 'SavingProductSearchInput',
  data() {
    return {
      payload: {
        depositAmount: '1000000',  // 예치금액
        selectedTerm: '12', // 초기 선택된 예치기간
        interest: '',  // 이자율(input)
        selectedPaymentTerm: '전체',  // 지급방식
        selectedRegion: '전체',  // 지역
        selectBank: '전체',  // 은행명
        selectedJoinChannel: '전체',
      },
      terms: [
        '6',
        '12',
        '24',
        '36' 
      ],
      paymentTerms: [
        '전체', 
        '단리', 
        '복리'],
      regions: [
        '전체',
        '서울',
        '부산',
        '대구',
        '인천',
        '광주',
        '대전',
        '울산',
        '세종',
        '경기도',
        '강원도',
        '충청북도',
        '충청남도',
        '전라북도',
        '전라남도',
        '경상북도',
        '경상남도',
        '제주'
      ],
      banks: [
          '전체',
          '우리은행',
          '한국스탠다드차타드은행',
          '대구은행',
          '부산은행',
          '광주은행',
          '제주은행',
          '전북은행',
          '경남은행',
          '중소기업은행',
          '한국산업은행',
          '국민은행',
          '신한은행',
          '농협은행주식회사',
          '하나은행',
          '주식회사 케이뱅크',
          '수협은행',
          '주식회사 카카오뱅크',
          '토스뱅크 주식회사',
      ],
      joinChannels: [
        '전체', 
        '온라인', 
        '방문'
      ],
    }
  },
  methods: {
    searchProducts() {
      this.$emit('search-bank', this.payload)
    }
  }
}
</script>

<style>

/* 화면에 보여지는 영역 */

.input_group {
  display: flex;
}

.input_group.all {
  display: block;
  padding: 10px 0px;
}

/* 화면에 보여지는 영역 */

.left_wrap {
  border-radius: 20px;
  width: 300px;
  height: 900px;
  background-color: #fff;
}

.tit{
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
  background-color: #6da36f;
  padding: 25px;
}


.left_menu_inner > * {
  width: 100%;
  display: block;
  background-color: #fff;
  
}

.input_box, .btn_wrap{
  margin-bottom: 10px;
  margin: auto;
  text-align: center;
}

.btn{
  width: 250px;
  height: 40px;
}

.input_box>input, select{
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px;
  width: 250px; 
  height: 35px;
  
}

.input_title>*{
  padding: 5px 27px;
  float: left;
}

.input_label{
  padding: 5px 27px;
  float:left
}

.head_txt{
  font-size: 24px;
  color: white;
}
span{
  color: white;
}


</style>