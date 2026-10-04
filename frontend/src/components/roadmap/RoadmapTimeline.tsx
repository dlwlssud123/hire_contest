import React from 'react';
import { ActionPlanStep } from '../../types';

interface Props {
  targetJob: string;
  totalWeeks: number;
  plans: ActionPlanStep[];
}

export const RoadmapTimeline: React.FC<Props> = ({ targetJob, totalWeeks, plans }) => {
  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
      <div className="border-b border-slate-100 pb-4 mb-6">
        <span className="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded">
          Career Navigation Plan
        </span>
        <h2 className="text-xl font-bold text-slate-900 mt-2">
          {targetJob} 달성을 위한 {totalWeeks}주 취업 최적 경로
        </h2>
        <p className="text-sm text-slate-500 mt-1">
          현재 보유 역량과 Skill Gap 우선순위, 고용24 연계 교육과정을 바탕으로 자동 최적화된 로드맵입니다.
        </p>
      </div>

      <div className="relative border-l-2 border-blue-200 ml-4 pl-6 space-y-8">
        {plans.map((plan, idx) => (
          <div key={idx} className="relative group">
            <div className="absolute -left-[31px] top-1 w-4 h-4 rounded-full bg-blue-600 border-4 border-white shadow" />
            <div className="bg-slate-50 rounded-lg p-5 border border-slate-200 hover:border-blue-400 transition">
              <span className="text-xs font-bold text-blue-700 bg-blue-100 px-2 py-0.5 rounded">
                {plan.weekRange}
              </span>
              <h4 className="text-lg font-bold text-slate-900 mt-1">{plan.title}</h4>
              <p className="text-sm text-slate-600 mt-1">{plan.goal}</p>

              <div className="mt-3 space-y-1">
                <p className="text-xs font-bold text-slate-700">권장 실행 과제:</p>
                <ul className="list-disc list-inside text-xs text-slate-600 space-y-0.5">
                  {plan.recommendedActivities.map((act, i) => (
                    <li key={i}>{act}</li>
                  ))}
                </ul>
              </div>

              {plan.linkedTrainings.length > 0 && (
                <div className="mt-3 pt-3 border-t border-slate-200 flex items-center gap-2">
                  <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded">
                    고용24 훈련과정 연계
                  </span>
                  <span className="text-xs text-slate-600 font-medium">
                    {plan.linkedTrainings.map(t => t.name).join(', ')}
                  </span>
                </div>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
