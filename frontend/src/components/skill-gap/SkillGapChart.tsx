import React from 'react';
import { SkillGapItem } from '../../types';

interface Props {
  skills: SkillGapItem[];
  readinessRate: number;
}

export const SkillGapChart: React.FC<Props> = ({ skills, readinessRate }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="flex justify-between items-center mb-6">
        <div>
          <h3 className="text-lg font-bold text-slate-900">노동시장 요구역량 vs 보유역량 (Skill Gap)</h3>
          <p className="text-sm text-slate-500">실제 고용24 채용공고 빅데이터 기반 출현 빈도 분석</p>
        </div>
        <div className="text-right">
          <span className="text-sm text-slate-500">현재 목표 직무 준비도</span>
          <div className="text-2xl font-black text-blue-600">{readinessRate}%</div>
        </div>
      </div>

      <div className="space-y-4">
        {skills.map((item) => (
          <div key={item.skillName} className="space-y-1">
            <div className="flex justify-between text-sm">
              <span className="font-semibold text-slate-800 flex items-center gap-2">
                {item.skillName}
                {item.isPossessed ? (
                  <span className="bg-emerald-100 text-emerald-700 text-xs px-2 py-0.5 rounded-full font-bold">보유</span>
                ) : (
                  <span className="bg-rose-100 text-rose-700 text-xs px-2 py-0.5 rounded-full font-bold">보완 필요</span>
                )}
              </span>
              <span className="text-slate-600 font-medium">채용공고 출현 빈도 {item.demandFrequency}%</span>
            </div>
            <div className="w-full bg-slate-100 rounded-full h-3 overflow-hidden">
              <div
                className={`h-full rounded-full transition-all duration-500 ${
                  item.isPossessed ? 'bg-emerald-500' : 'bg-rose-400'
                }`}
                style={{ width: `${item.demandFrequency}%` }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
