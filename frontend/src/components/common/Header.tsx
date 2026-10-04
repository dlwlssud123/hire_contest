import React from 'react';

export const Header: React.FC = () => {
  return (
    <header className="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-50">
      <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="w-9 h-9 bg-blue-600 rounded-lg flex items-center justify-center font-bold text-lg">
            CP
          </div>
          <div>
            <h1 className="font-bold text-lg leading-tight">CareerPath AI</h1>
            <p className="text-xs text-slate-400">공공데이터 기반 개인 맞춤형 AI 취업 내비게이션</p>
          </div>
        </div>
        <nav className="flex space-x-6 text-sm font-medium">
          <a href="/profile" className="text-slate-300 hover:text-white transition">내 프로필</a>
          <a href="/jobs" className="text-slate-300 hover:text-white transition">AI 직무추천</a>
          <a href="/skill-gap" className="text-slate-300 hover:text-white transition">Skill Gap 분석</a>
          <a href="/roadmap" className="text-blue-400 hover:text-blue-300 transition">취업 내비게이션</a>
          <a href="/simulation" className="text-slate-300 hover:text-white transition">What-if 시뮬레이션</a>
          <a href="/report" className="text-slate-300 hover:text-white transition">취업 전략 보고서</a>
          <a href="/chat" className="text-slate-300 hover:text-white transition">AI 커리어 에이전트</a>
        </nav>
      </div>
    </header>
  );
};
