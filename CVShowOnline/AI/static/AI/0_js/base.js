china_map();  //下面封装成函数，在这里调用
pie_fanzui();
current_time();
pie_age();
time_line();
// 中间板块的中国地图，获取数据调用的接口是'/AI/people_origin_get'
function china_map() {
    var myChart = echarts.init(document.getElementById('china_map'),'infographic');//初始化echarts容器

      $.ajax({
          url:'/AI/people_origin_get',
          type:'get',
          dataType:'json',
            success:function(res){
           console.log(res)
                datalist = res['data']//如果直接用res 表示的是{'data':[{},{},{}]}是一个字典

                option = {
                    title: {
                        text: '犯罪人口来源分析',
                        textStyle:{color:'#fff'},
                        //subtext: '纯属虚构',
                        x:'center'
                    },
                    tooltip : {
                        trigger: 'item'
                    },
                    visualMap: {
                        show : false,
                        x: 'left',
                        y: 'bottom',
                        //layoutCenter:['30%','30%'],
                        splitList: [
                            {start: 500, end:600},{start: 400, end: 500},
                            {start: 300, end: 400},{start: 200, end: 300},
                            {start: 100, end: 200},{start: 0, end: 100},
                        ],
                        color: ['#ff0', '#ffff00', '#0E94EB','#6FBCF0', '#F0F06F', '#00CC00']
                    },
                    series: [{
                        name: '犯罪人口来源分析',
                        type: 'map',
                        mapType: 'china',
                        roam: true,
                        label: {
                            normal: {
                                show: false
                            },
                            emphasis: {
                                show: false
                            }
                        },
                        data:datalist
                    }]
                };
                myChart.setOption(option);
                        }
                  })



}

//违法犯罪人员分析占比，带边框效果的饼图
function pie_fanzui(){

    var pie_fanzui =echarts.init(document.getElementById("pie_fanzui"),'infographic');
    $.ajax({
        url:'/AI/crime_analyze_get/',
        type:'get',
        dataType:'json',
        success:function(res){
            console.log(res)
             crime_analyze_data = res['data']
            option = {
            title : {
                x:'center'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            legend: {
                orient: 'vertical',
                left: 'left',
                data: ['卖淫嫖娼','经侦嫌疑','重点人口','刑贞重点','吸毒人口'],
                textStyle: {color: '#fff'}
            },

            label: {
                 normal: {
                      textStyle: {
                            color: 'red'  // 改变标示文字的颜色
                      }
                 }
            },
            series : [
                {
                    name: '违法犯罪人员分析',
                    type: 'pie',
                    radius : '55%',
                    center: ['50%', '60%'],
                    data:crime_analyze_data,
                    // [
                    //     {value:335, name:'卖淫嫖娼'},
                    //     {value:310, name:'经侦嫌疑'},
                    //     {value:234, name:'重点人口'},
                    //     {value:135, name:'刑贞重点'},
                    //     {value:1548, name:'吸毒人口'}
                    // ],

                    itemStyle: {
                        emphasis: {
                            shadowBlur: 10,
                            shadowOffsetX: 0,

                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }
                    }

                }
            ]
        };
            pie_fanzui.setOption(option);

        }
    });

//----------------------违法犯罪人员分析占比end---------------

}

//违法犯罪人员年龄分析占比，带边框效果的饼图
function pie_age() {
//var pie_age =echarts.init(document.getElementById("pie_age"),'macarons');
var pie_age =echarts.init(document.getElementById("pie_age"),'infographic');
//var pie_age =echarts.init(document.getElementById("pie_age"),'shine');

$.ajax({
        url:'/AI/age_distribution_get/',
        type:'get',
        dataType:'json',
        success:function(res){
            console.log(res)
            var age_distribution_data = res['data']
            option = {
                tooltip: {
                    trigger: 'item',
                    formatter: "{a} <br/>{b}: {c} ({d}%)"
                },
                legend: {
                    orient: 'vertical',
                    x: 'left',
                    data:['18-30','31-40','41-50','51-60','65岁以上','未标明'],
                    textStyle: {color: '#fff'}
                },
                series: [
                    {
                        name:'违法犯罪人员年龄分布',
                        type:'pie',
                        radius: ['30%', '55%'],
                        avoidLabelOverlap: false,
                        label: {
                            normal: {
                                show: false,
                                position: 'center'
                            },
                            emphasis: {
                                show: true,
                                textStyle: {
                                    fontSize: '20',
                                    fontWeight: 'bold'
                                }
                            }
                        },
                        labelLine: {
                            normal: {
                                show: false
                            }
                        },
                        data:age_distribution_data
                    }
                ]
            };
            pie_age.setOption(option);

        }
    });

//----------------------违法犯罪人员年龄分析占比end---------------

}

//===================人口出入时间段统计=======================
function time_line(){
//var line_time =echarts.init(document.getElementById("line_time"),'shine');
var line_time =echarts.init(document.getElementById("line_time"),'macarons');
//var line_time =echarts.init(document.getElementById("line_time"),'infographic');
$.ajax({
        url:'/AI/time_line_get/',
        type:'get',
        dataType:'json',
        success:function(res){
            console.log(res);
             time_line_value = res['data_value'];
            option = {
                    // 给echarts图设置背景色
                    //backgroundColor: '#FBFBFB',  // -----------> // 给echarts图设置背景色
                    color: ['#7FFF00'],
                    tooltip: {
                        trigger: 'axis'
                    },

                    grid:{
                                x:40,
                                y:30,
                                x2:5,
                                y2:20

                            },
                    calculable: true,


                    xAxis: [{
                         type: 'category',
                    data:[ "6:00-9:00",  "10:00-12:00",  "13:00-15:00",  "16:00-20:00",  "18:00-21:00", "21:00-24:00"  ],
                 axisLabel: {
                        color: "#7FFF00" //刻度线标签颜色
                        }
                    }],
                    yAxis: [{

                        type: 'value',
                        axisLabel: {
                        color: "#7FFF00" //刻度线标签颜色
                        }
                    }],
                    series: [{
                        name: '人次',
                        type: 'line',
                        data:time_line_value ,

                    }]
                            };


            line_time.setOption(option);
        }
    });


}

//=========违法犯罪人员地区分布开始=======================
//var qufenbu_data =echarts.init(document.getElementById("qufenbu_data"),'shine'); 
//var qufenbu_data =echarts.init(document.getElementById("qufenbu_data"),'macarons'); 
var qufenbu_data =echarts.init(document.getElementById("qufenbu_data"),'infographic'); 
option = {
    color: ['#FADB71'],
    tooltip : {
        trigger: 'axis',
        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
        }
    },
    grid: {
        x:30,
        y:10,
        x2:15,
        y2:20
    },
    xAxis : [
        {
            type : 'category',
            data : ['河北', '天津', '北京', '新疆', '内蒙', '宁夏', '海南'],
            axisTick: {
                alignWithLabel: true
            },
            axisLabel: {
			color: "#FADB71" //刻度线标签颜色
			}
        }
    ],
    yAxis : [
        {
            type : 'value',
            axisLabel: {
			color: "#FADB71" //刻度线标签颜色
			}
        }
    ],
    series : [
        {
            name:'地区分布',
            type:'bar',
            barWidth: '60%',
            data:[10, 52, 200, 334, 390, 330, 220]
        }
    ]
};

qufenbu_data.setOption(option);
//=========违法犯罪人员地区分布结束=======================


//时间选择器
var startV = '';
var endV = '';
laydate.skin('danlan');
var startTime = {
    elem: '#startTime',
    format: 'YYYY-MM-DD',
    min: '1997-01-01', //设定最小日期为当前日期
    max: laydate.now(), //最大日期
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        startV = datas;
        endTime.min = datas; //开始日选好后，重置结束日的最小日期
    }
};
var endTime = {
    elem: '#endTime',
    format: 'YYYY-MM-DD',
    min: laydate.now(),
    max: laydate.now(),
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        endV = datas;
    }
};

laydate(startTime);
laydate(endTime);

//时间选择器
var startVs = '';
var endVs = '';
laydate.skin('danlan');
var startTimes = {
    elem: '#startTimes',
    format: 'YYYY-MM-DD',
    min: '1997-01-01', //设定最小日期为当前日期
    max: '2099-06-16', //最大日期
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        startVs = datas;
        endTimes.min = datas; //开始日选好后，重置结束日的最小日期
        setQgData($('#barTypes').parent().parent(), 1);
    }
};
var endTimes = {
    elem: '#endTimes',
    format: 'YYYY-MM-DD',
    min: laydate.now(),
    max: laydate.now(),
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        endVs = datas;
        setQgData($('#barTypes').parent().parent(), 1);
    }
};

laydate(startTimes);
laydate(endTimes);




//更改日期插件的样式
function dateCss() {
    var arr = $('#laydate_box').attr('style').split(';');
    var cssStr =
        'position:absolute;right:0;';
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].indexOf('top') != -1) {
            cssStr += arr[i];
        }
    }

    $('#laydate_box').attr('style', cssStr);
}


var workDate;
var time = {
    elem: '#times',
    format: 'YYYY-MM-DD',
    min: laydate.now(),
    max: laydate.now() + 30,
    istime: true,
    istoday: true,
    fixed: false,
    choose: function (datas) {
        //        startTime.max = datas; //结束日选好后，重置开始日的最大日期
        workDate = datas;
    }
};

laydate(time);


function fnW(str) {
    var num;
    str >= 10 ? num = str : num = "0" + str;
    return num;
}
//获取当前时间
function current_time() {
    var timer = setInterval(function () {
    var date = new Date();
    var year = date.getFullYear(); //当前年份
    var month = date.getMonth(); //当前月份
    var data = date.getDate(); //天
    var hours = date.getHours(); //小时
    var minute = date.getMinutes(); //分
    var second = date.getSeconds(); //秒
    var day = date.getDay(); //获取当前星期几
    var ampm = hours < 12 ? 'am' : 'pm';
    $('#time').html(fnW(hours) + ":" + fnW(minute) + ":" + fnW(second));
    $('#date').html('<span>' + year + '/' + (month + 1) + '/' + data + '</span><span>' + ampm + '</span><span>周' + day + '</span>')

}, 1000)
}

