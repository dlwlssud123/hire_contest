import React, { useState } from 'react';
import { AgentChatMessage } from '../../types';

export const CareerAgentChat: React.FC = () => {
  const [messages, setMessages] = useState<AgentChatMessage[]>([
    {
      role: 'assistant',
      content: '안녕하세요! 취업 내비게이션 AI Career Agent입니다. 희망하는 직무, 남은 준비 기간, 희망 지역 등 변경 사항이 있으시면 말씀해주세요. 실시간으로 로드맵을 재설계해드립니다.',
    },
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;
    const userMsg: AgentChatMessage = { role: 'user', content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput('');

    // Mock AI reply
    setTimeout(() => {
      let replyContent = `말씀해주신 조건("${userMsg.content}")을 반영하여 노동시장 데이터와 Skill Gap을 다시 분석했습니다.`;
      if (userMsg.content.includes('3개월')) {
        replyContent = '3개월 단기 집중 경로로 로드맵을 재설계했습니다. 우선순위가 높은 핵심 기술(Spring/AWS) 중심의 압축 플랜이 반영되었습니다.';
      }
      setMessages((prev) => [...prev, { role: 'assistant', content: replyContent }]);
    }, 600);
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 flex flex-col h-[520px]">
      <div className="p-4 border-b border-slate-100 flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 bg-emerald-500 rounded-full animate-pulse" />
          <h3 className="font-bold text-slate-800 text-sm">대화형 AI Career Agent (Dynamic Re-planning)</h3>
        </div>
        <span className="text-xs bg-slate-100 text-slate-600 px-2 py-1 rounded font-medium">고용24 RAG 연동</span>
      </div>

      <div className="flex-1 p-4 overflow-y-auto space-y-3">
        {messages.map((m, idx) => (
          <div
            key={idx}
            className={`flex ${m.role === 'user' ? 'justify-end' : 'justify-start'}`}
          >
            <div
              className={`max-w-md rounded-xl p-3.5 text-sm ${
                m.role === 'user'
                  ? 'bg-blue-600 text-white rounded-br-none'
                  : 'bg-slate-100 text-slate-800 rounded-bl-none'
              }`}
            >
              {m.content}
            </div>
          </div>
        ))}
      </div>

      <div className="p-3 border-t border-slate-100 flex gap-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="예: '취업까지 3개월밖에 없어', '서울 지역 채용공고도 포함해줘'"
          className="flex-1 text-sm border border-slate-200 rounded-lg px-3.5 py-2 outline-none focus:border-blue-500"
        />
        <button
          onClick={handleSend}
          className="bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-4 py-2 rounded-lg transition"
        >
          전송
        </button>
      </div>
    </div>
  );
};
