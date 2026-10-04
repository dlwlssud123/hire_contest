import React from 'react';
import { Header } from '../components/common/Header';
import { SkillGapChart } from '../components/skill-gap/SkillGapChart';
import { RoadmapTimeline } from '../components/roadmap/RoadmapTimeline';
import { WhatIfSimulator } from '../components/simulation/WhatIfSimulator';
import { CareerAgentChat } from '../components/chat/CareerAgentChat';

export default function Home() {
  const mockSkills = [
    { skillName: 'Java', demandFrequency: 78, isPossessed: true, priorityLevel: 'High' as const, learningWeeks: 3, recommendedTrainings: [], recommendedCertifications: [] },
    { skillName: 'Spring Boot', demandFrequency: 71, isPossessed: false, priorityLevel: 'High' as const, learningWeeks: 4, recommendedTrainings: ['Spring 웹 백엔드 실무'], recommendedCertifications: [] },
    { skillName: 'SQL', demandFrequency: 63, isPossessed: true, priorityLevel: 'High' as const, learningWeeks: 2, recommendedTrainings: [], recommendedCertifications: ['SQLD'] },
    { skillName: 'AWS', demandFrequency: 45, isPossessed: false, priorityLevel: 'Medium' as const, learningWeeks: 3, recommendedTrainings: ['AWS 클라우드 아키텍처'], recommendedCertifications: [] },
    { skillName: 'Docker', demandFrequency: 38, isPossessed: false, priorityLevel: 'Medium' as const, learningWeeks: 2, recommendedTrainings: ['컨테이너 기초 실습'], recommendedCertifications: [] },
  ];

  const mockPlans = [
    {
      weekRange: '1~4주차',
      title: 'Spring Boot 학습 및 REST API 프로젝트 개발',
      goal: 'Spring Boot 3.x 프레임워크 핵심 이해 및 CRUD 포트폴리오 구축',
      recommendedActivities: ['Spring Data JPA 실습', 'REST API 설계 및 테스트 코드 작성'],
      linkedTrainings: [{ name: 'K-디지털 트레이닝 백엔드 부트캠프', source: '고용24' }],
      linkedCertifications: [],
    },
    {
      weekRange: '5~6주차',
      title: 'Docker 컨테이너화 및 배포 환경 구성',
      goal: '애플리케이션 가상화 및 로컬/서버 배포 환경 일치화',
      recommendedActivities: ['Dockerfile 작성 및 멀티 스테이지 빌드', 'Docker Compose 연동'],
      linkedTrainings: [],
      linkedCertifications: [],
    },
    {
      weekRange: '7~8주차',
      title: 'AWS 클라우드 배포 및 CI/CD 구축',
      goal: '실제 운영 환경 배포 경험 및 자동화 파이프라인 완성',
      recommendedActivities: ['AWS EC2/RDS 인프라 설정', 'GitHub Actions 배포 파이프라인'],
      linkedTrainings: [{ name: 'AWS 클라우드 실습 과정', source: '고용24' }],
      linkedCertifications: [],
    },
    {
      weekRange: '9~12주차',
      title: '목표 채용공고 지원 및 AI Career Agent 모의 면접',
      goal: '매칭률 높은 채용공고 5개사 집중 지원 및 면접 준비',
      recommendedActivities: ['포트폴리오 README 최적화', '예상 기술 면접 질문 답변 준비'],
      linkedTrainings: [],
      linkedCertifications: [{ name: '정보처리기사 실기', source: '한국산업인력공단' }],
    },
  ];

  return (
    <div className="min-h-screen bg-slate-100 text-slate-900 flex flex-col">
      <Header />
      <main className="max-w-7xl mx-auto px-4 py-8 space-y-8 flex-1 w-full">
        {/* Hero Section */}
        <section className="bg-gradient-to-r from-blue-700 to-indigo-800 text-white rounded-2xl p-8 shadow-md">
          <span className="bg-blue-500/30 text-blue-100 text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider">
            AI 고용서비스 혁신 프로젝트
          </span>
          <h2 className="text-3xl font-extrabold mt-3 leading-tight">
            공공데이터 기반 개인 맞춤형 AI 취업 내비게이션
          </h2>
          <p className="text-blue-100 mt-2 max-w-2xl text-sm leading-relaxed">
            채용공고 나열을 넘어 사용자의 현재 위치에서 목표 직무까지 최적의 취업 경로를 계산합니다.
            고용24 빅데이터와 연계한 Skill Gap 분석, 맞춤형 주차별 Action Plan, What-if 시뮬레이션을 경험해보세요.
          </p>
        </section>

        {/* Core Features Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <SkillGapChart skills={mockSkills} readinessRate={65} />
          <WhatIfSimulator />
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2">
            <RoadmapTimeline targetJob="백엔드 개발자" totalWeeks={12} plans={mockPlans} />
          </div>
          <div>
            <CareerAgentChat />
          </div>
        </div>
      </main>
    </div>
  );
}
