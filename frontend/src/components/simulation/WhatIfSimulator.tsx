import React, { useState } from 'react';
import { SimulationResult } from '../../types';

export const WhatIfSimulator: React.FC = () => {
  const [selectedActivities, setSelectedActivities] = useState<string[]>(['Spring 프로젝트 추가', 'Docker 학습']);
  const [currentScore, setCurrentScore] = useState(58);
  const [simulatedScore, setSimulatedScore] = useState(82);

  const availableOptions = [
    { name: 'Spring 프로젝트 추가', weeks: 4, score: 18 },
    { name: '정보처리기사 취득', weeks: 8, score: 6 },
    { name: 'Docker 학습', weeks: 2, score: 8 },
    { name: 'AWS 프로젝트 배포', weeks: 5, score: 12 },
  ];

  const toggleOption = (name: string) => {
    setSelectedActivities((prev) =>
      prev.includes(name) ? prev.filter((item) => item !== name) : [...prev, name]
    );
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="border-b border-slate-100 pb-4 mb-6">
        <h3 className="text-lg font-bold text-slate-900">What-if 취업 시뮬레이터 (준비도 변화 예측)</h3>
        <p className="text-sm text-slate-500">
          학습 활동이나 자격증을 추가했을 때 채용 요구조건 충족도(준비도 점수)가 어떻게 변화하는지 확인해보세요.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="space-y-3">
          <label className="text-xs font-bold text-slate-700 uppercase">시뮬레이션 활동 선택</label>
          {availableOptions.map((opt) => {
            const isChecked = selectedActivities.includes(opt.name);
            return (
              <div
                key={opt.name}
                onClick={() => toggleOption(opt.name)}
                className={`flex items-center justify-between p-3 rounded-lg border cursor-pointer transition ${
                  isChecked
                    ? 'border-blue-500 bg-blue-50/50 text-blue-900'
                    : 'border-slate-200 hover:border-slate-300 bg-white text-slate-700'
                }`}
              >
                <div>
                  <span className="font-semibold text-sm">{opt.name}</span>
                  <span className="text-xs text-slate-400 ml-2">({opt.weeks}주 소요)</span>
                </div>
                <span className="text-xs font-bold text-blue-600">+{opt.score}점</span>
              </div>
            );
          })}
        </div>

        <div className="bg-slate-50 rounded-xl p-6 flex flex-col justify-center items-center border border-slate-200 text-center">
          <span className="text-xs font-bold text-slate-500">예상 취업 준비도 변화</span>
          <div className="flex items-center gap-4 my-4">
            <div>
              <span className="text-xs text-slate-400">현재</span>
              <div className="text-3xl font-black text-slate-600">{currentScore}점</div>
            </div>
            <div className="text-2xl text-slate-400 font-bold">→</div>
            <div>
              <span className="text-xs text-blue-600 font-bold">시뮬레이션 후</span>
              <div className="text-4xl font-black text-blue-600">{simulatedScore}점</div>
            </div>
          </div>
          <p className="text-xs text-slate-500 max-w-xs">
            * 채용공고 요구조건 대비 역량 충족도를 나타내며 실제 취업 합격 확률과는 차이가 있을 수 있습니다.
          </p>
        </div>
      </div>
    </div>
  );
};
