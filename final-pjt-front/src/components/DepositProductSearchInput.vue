<template>
 
  <div class="wrap">
    <div id="container" class="saving_main">
    <form class="m-1" @submit.prevent="searchProducts">
      <!-- 좌측 검색필터 -->
      <div class="left_menu">
          <div class="left_wrap fixed shadow">
              <p class="tit">
                  <strong>정기예금</strong><br>
                  검색조건을 입력해주세요
              </p>

              <div class="filters cs_scroll">
                  <div class="left_menu_inner">

                      <!-- 1. 예치금액 -->
                      <div class="amount_area">
                        <label class="input_label"><span class="txt">예치금액</span></label>
                        <div class="input_box">
                          <input class="min amount" name="amount" maxlength="10" v-model="depositAmount">
                        </div>
                      </div>

                      <!-- 2. 예치기간 -->
                      <div class="input_group all period">
                        <label class="input_label">예치기간</label>
                        <div class="input_box">
                          <select class="min select" name="term" v-model="selectedTerm">
                            <option v-for="term in terms" :key="term" :value="term">{{ term }}</option>
                          </select>
                        </div>
                      </div>


                      <!-- 3. 이자율 -->
                      <div class="amount_area">
                        <label class="input_label"><span class="txt">이자율</span></label>
                        <div class="input_box">
                          <input class="min interest" v-model="interest" name="interest" maxlength="10">
                        </div>
                      </div>
                      
                      <!-- 4. 이자지급방식 -->
                      <div class="input_group all deposit_only" style="display: block;">
                        <label class="input_label">이자지급방식</label>
                        <div class="input_box">
                          <select class="min select" v-model="selectedPaymentTerm" name="payment_term">
                            <option v-for="option in paymentTerms" :key="option" :value="option">{{ option }}</option>
                          </select>
                        </div>
                      </div>

                      <!-- 5. 지역 -->
                      <div class="input_group all">
                        <label class="input_label">지역</label>
                        <div class="input_box">
                          <select class="min select" v-model="selectedRegion" name="region_sido">
                            <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
                          </select>
                        </div>
                      </div>


                      <!-- 6. 은행명 -->
                      <div class="input_gruop all">
                        <label class="input_label">은행명</label>
                        <div class="input_box">
                          <select class="min select" v-model="selectBank" name="bank_sido">
                            <option v-for="bank in banks" :key="bank" :value="bank">{{ bank }}</option>
                          </select>
                        </div>
                      </div>

                      <!-- <b-form-group label="은행명" label-for="bank" label-cols-md="auto" class="mb-3">
                        <b-form-select id="bank" v-model="selectBank" :options="banks"></b-form-select>
                      </b-form-group> -->



                      <!-- 7. 가입방식 -->
                      <div class="input_group all">
                        <label class="input_label">가입방식</label>
                        <div class="input_box">
                          <select class="min select" v-model="selectedJoinChannel" name="join_channel">
                            <option v-for="channel in joinChannels" :key="channel" :value="channel">{{ channel }}</option>
                          </select>
                        </div>
                      </div>


                      <!-- 확인 / 초기화  -->
                      <div class="btn_wrap">
                          <!-- <button class="mi_btn color" id="goNext">검색</button> -->
                          <button type="submit" class="btn btn-primary">조회</button>
                          <button class="btn_reset">초기화</button>
                      </div>

                  </div>


                    
                      
              </div>
          </div>

      </div>
      </form>
      <div class="right_contents">

      </div>
    </div>


  </div>
</template>

<script>
export default {
  name: 'SavingProductSearchInput',
  data() {
    return {
      depositAmount: '1000000',
      selectedTerm: '12개월', // 초기 선택된 예치기간
      terms: [
        '6개월',
        '12개월',
        '24개월',
        '36개월' 
      ],
      interest: '',
      selectedPaymentTerm: '전체',
      paymentTerms: [
        '전체', 
        '단리', 
        '복리'],
      selectedRegion: '전체',
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
      selectBank: '전체',
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
      selectedJoinChannel: '전체',
      joinChannels: [
        '전체', 
        '온라인', 
        '방문'
      ]
    }
  },
  methods: {
    searchProducts() {
      this.$emit('search-bank', this.bank)
    }
  }
}
</script>

<style scoped>

.input_group {
  display: flex;
}

.input_group.all {
  display: block;
}

/* 화면에 보여지는 영역 */
#container {
  padding-top: 90px;
  padding-bottom: 90px;
  width: 1200px;
  margin: 0 auto;
}

#container > div {
  float: left;
}

#container .left_menu {
  width: 300px;
  min-height: -moz-calc( 100vh - 220px);
  min-height: calc( 100vh - 220px);
}

/* .saving_main .left_wrap {
  padding-top: 39px;
} */

.left_menu_inner > * {
  width: 100%;
  display: block;
  margin-bottom: 10px;
}



</style>

